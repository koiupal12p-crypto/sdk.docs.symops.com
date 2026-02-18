import os
import random
import string
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class SitemapScraper:
    def __init__(self):
        # قائمة الـ Sitemaps التي تريد مراقبتها
        self.sitemaps = [
            "https://aawsat.com/sitemap.xml",
            # أضف الروابط الأخرى هنا
        ]
        self.db_file = "processed_urls.txt"
        self.processed_urls = self.load_processed_urls()

    def load_processed_urls(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, "r") as f:
                return set(line.strip() for line in f)
        return set()

    def save_url(self, url):
        with open(self.db_file, "a") as f:
            f.write(url + "\n")
        self.processed_urls.add(url)

    def get_latest_urls(self):
        new_articles = []
        for sitemap_url in self.sitemaps:
            try:
                # 1. الدخول للـ Sitemap الرئيسي لجلب آخر صفحة
                r = requests.get(sitemap_url, timeout=10)
                # بحث عن الروابط الفرعية (loc)
                pages = re.findall(r'<loc>(.*?)</loc>', r.text)
                if not pages: continue
                
                # الدخول لآخر صفحة سيت ماب (الأحدث عادة تكون الأخيرة أو المحددة بـ page=X)
                latest_page_url = pages[-1] 
                r_page = requests.get(latest_page_url, timeout=10)
                urls = re.findall(r'<loc>(.*?)</loc>', r_page.text)
                
                for url in reversed(urls): # نبدأ من الأحدث
                    if url not in self.processed_urls and ".html" in url or "aawsat.com" in url:
                        if len(new_articles) < 5: # سحب 5 مقالات جديدة فقط في كل دورة
                            data = self.scrape_article(url)
                            if data:
                                new_articles.append(data)
                                self.save_url(url)
            except Exception as e:
                print(f"Error fetching sitemap: {e}")
        return new_articles

    def scrape_article(self, url):
        try:
            r = requests.get(url, timeout=10)
            soup = BeautifulSoup(r.content, 'html.parser')
            
            # استخلاص العنوان والوصف (تعديل الـ selectors حسب الموقع)
            title = soup.find('h1').get_text(strip=True) if soup.find('h1') else ""
            # محاولة جلب الوصف من meta tag أو أول فقرة
            desc = ""
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                desc = meta_desc['content']
            else:
                p_tag = soup.find('p')
                desc = p_tag.get_text(strip=True) if p_tag else "No description available"

            if title:
                return {"title": title, "desc": desc, "url": url}
        except:
            return None
        return None

class ContinuousGenerator:
    def __init__(self):
        self.templates = {}
        self.template_names = ["test.html", "test1.html", "test2.html"]
        self.domain = self.load_domain()
        self.load_all_templates()
        self.scraper = SitemapScraper()

    def load_all_templates(self):
        for t_name in self.template_names:
            if os.path.exists(t_name):
                with open(t_name, "r", encoding="utf-8") as f:
                    self.templates[t_name] = f.read()

    def load_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r", encoding="utf-8") as f:
                return f.read().strip().replace("https://", "")
        return "example.org"

    def run_cycle(self):
        articles = self.scraper.get_latest_urls()
        if not articles:
            print("No new articles found.")
            return

        for article in articles:
            # تنظيف العنوان لعمل رابط URL
            clean_name = re.sub(r'[^\w\s-]', '', article['title'].lower())
            slug = re.sub(r'[-\s]+', '-', clean_name).strip('-')[:80]
            
            folder = "news"
            os.makedirs(folder, exist_ok=True)
            
            filename = f"{slug}.html"
            template_content = self.templates.get(random.choice(self.template_names), "")
            
            content = template_content.replace("{{TITLE}}", article['title'])
            content = content.replace("{{DESCRIPTION}}", article['desc'])
            content = content.replace("{{CANONICAL_URL}}", f"https://{self.domain}/{folder}/{filename}")
            content = content.replace("{{DOMAIN_NAME}}", self.domain)
            content = content.replace("{{DATE}}", datetime.utcnow().isoformat())
            content = content.replace("{{INTERNAL_LINKS}}", "")

            with open(os.path.join(folder, filename), "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ Generated: {filename}")

if __name__ == "__main__":
    gen = ContinuousGenerator()
    gen.run_cycle()
