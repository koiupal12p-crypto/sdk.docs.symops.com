import os
import random
import string
import re
from datetime import datetime, timedelta

# ==============================================================================
# GENERATOR PRO - ADVANCED INTERNAL LINKING EDITION
# - Absolute internal links (SEO safe)
# - Smart internal linking:
#     * 3 links from same folder (cluster boost)
#     * 2 links from different folders (crawl depth boost)
# - No duplicate links
# - Canonical URL auto-generated
# - Domain auto-detected from CNAME
# - GitHub Actions optimized
# ==============================================================================

class ContinuousGenerator:
    def __init__(self):
        self.templates = {}
        self.template_names = ["test.html", "test1.html", "test2.html"]
        self.keywords_ar = []
        self.keywords_en = []
        self.max_files_per_folder = 500
        self.emojis = ["🔥", "🎥", "🔞", "😱", "✅", "🌟", "📺", "🎬", "✨", "💎", "⚡"]

        self.load_all_templates()
        self.load_keywords()
        self.domain = self.load_domain()

    # --------------------------------------------------------------------------
    # Load Templates
    # --------------------------------------------------------------------------
    def load_all_templates(self):
        for t_name in self.template_names:
            if os.path.exists(t_name):
                with open(t_name, "r", encoding="utf-8") as f:
                    self.templates[t_name] = f.read()
                print(f"[*] Template {t_name} loaded.")
            else:
                self.templates[t_name] = (
                    "<html><head>"
                    "<title>{{TITLE}}</title>"
                    "<link rel='canonical' href='{{CANONICAL_URL}}'>"
                    "</head><body>"
                    "<h1>{{TITLE}}</h1>"
                    "<p>{{DESCRIPTION}}</p>"
                    "{{INTERNAL_LINKS}}"
                    "</body></html>"
                )
                print(f"[!] {t_name} not found. Using fallback template.")

    # --------------------------------------------------------------------------
    # Load Keywords
    # --------------------------------------------------------------------------
    def load_keywords(self):
        if os.path.exists("keywords_ar.txt"):
            with open("keywords_ar.txt", "r", encoding="utf-8") as f:
                self.keywords_ar = [l.strip() for l in f if l.strip()]

        if os.path.exists("keywords_en.txt"):
            with open("keywords_en.txt", "r", encoding="utf-8") as f:
                self.keywords_en = [l.strip() for l in f if l.strip()]

        if not self.keywords_ar:
            self.keywords_ar = ["محتوى", "تقني", "تحديث"]
        if not self.keywords_en:
            self.keywords_en = ["tech", "update", "news"]

    # --------------------------------------------------------------------------
    # Load Domain from CNAME
    # --------------------------------------------------------------------------
    def load_domain(self):
        if os.path.exists("CNAME"):
            with open("CNAME", "r", encoding="utf-8") as f:
                domain = f.read().strip()
                domain = domain.replace("https://", "").replace("http://", "")
                return domain
        return "example.com"

    # --------------------------------------------------------------------------
    # Generate Random Text
    # --------------------------------------------------------------------------
    def build_text(self, min_words, max_words, mode="ar"):
        target_length = random.randint(min_words, max_words)
        source = self.keywords_ar if mode == "ar" else self.keywords_en
        words = []

        while len(words) < target_length:
            words.extend(random.choice(source).split())

        return " ".join(words[:target_length])

    # --------------------------------------------------------------------------
    # Create Folder Structure
    # --------------------------------------------------------------------------
    def get_target_path(self, total_count):
        paths = []
        files_remaining = total_count

        while files_remaining > 0:
            d1 = ''.join(random.choices(string.ascii_lowercase, k=3))
            d2 = ''.join(random.choices(string.ascii_lowercase, k=3))
            full_path = os.path.join(d1, d2)
            os.makedirs(full_path, exist_ok=True)
            paths.append(full_path)
            files_remaining -= self.max_files_per_folder

        return paths

    # --------------------------------------------------------------------------
    # Smart Internal Linking Builder
    # --------------------------------------------------------------------------
    def build_internal_links(self, current_index, generated_files):
        current_file = generated_files[current_index]
        current_folder = current_file["folder"]

        same_folder = []
        other_folders = []

        for idx, file in enumerate(generated_files):
            if idx == current_index:
                continue

            if file["folder"] == current_folder:
                same_folder.append(file)
            else:
                other_folders.append(file)

        random.shuffle(same_folder)
        random.shuffle(other_folders)

        selected_links = same_folder[:7] + other_folders[:2]

        links_html = (
            "<div style='margin-top:50px;padding:20px;border-top:2px solid #eee'>"
            "<h3>🔗 مقالات ذات صلة</h3><ul>"
        )

        for link in selected_links:
            full_link = f"https://{self.domain}/{link['folder']}/{link['filename']}"
            links_html += f"<li><a href='{full_link}'>{link['display_title']}</a></li>"

        links_html += "</ul></div>"

        return links_html

    # --------------------------------------------------------------------------
    # Run Generator Cycle
    # --------------------------------------------------------------------------
    def run_single_cycle(self, count=200):
        folder_paths = self.get_target_path(count)
        generated_files = []

        base_time = datetime.utcnow()

        for folder in folder_paths:
            for _ in range(min(count, self.max_files_per_folder)):
                title_text = self.build_text(5, 10)
                display_title = f"{random.choice(self.emojis)} {title_text} {random.choice(self.emojis)}"

                clean_name = re.sub(r'[^\w\s-]', '', title_text.lower())
                slug = re.sub(r'[-\s]+', '-', clean_name).strip('-')[:80]
                if not slug:
                    slug = ''.join(random.choices(string.ascii_lowercase, k=10))

                generated_files.append({
                    "display_title": display_title,
                    "filename": f"{slug}.html",
                    "desc": self.build_text(120, 220),
                    "folder": folder,
                    "date_iso": base_time.strftime("%Y-%m-%dT%H:%M:%S+00:00"),
                    "template": random.choice(self.template_names)
                })

        # Write Files
        for i, file_data in enumerate(generated_files):
            template_content = self.templates.get(file_data['template'], "")

            canonical_url = f"https://{self.domain}/{file_data['folder']}/{file_data['filename']}"
            internal_links = self.build_internal_links(i, generated_files)

            content = template_content
            content = content.replace("{{TITLE}}", file_data['display_title'])
            content = content.replace("{{DESCRIPTION}}", file_data['desc'])
            content = content.replace("{{CANONICAL_URL}}", canonical_url)
            content = content.replace("{{INTERNAL_LINKS}}", internal_links)
            content = content.replace("{{DOMAIN_NAME}}", self.domain)

            target_file = os.path.join(file_data['folder'], file_data['filename'])
            with open(target_file, "w", encoding="utf-8") as f:
                f.write(content)

        print(f"✅ Generated {len(generated_files)} pages with smart internal linking.")


if __name__ == "__main__":
    generator = ContinuousGenerator()
    generator.run_single_cycle(count=100)
