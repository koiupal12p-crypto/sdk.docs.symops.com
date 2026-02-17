import os

# الروابط المطلوبة مع كلمات مفتاحية متنوعة (Dofollow)
links_to_inject = """
<footer style="opacity: 0.8; font-size: 12px; border-top: 1px solid #eee; margin-top: 50px; padding: 10px; direction: rtl;">
    <p>روابط مفيدة: 
        <a href="https://www.pjh.is/" rel="dofollow">Pjh الرئيسية</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%B4%D8%B1%D9%85%D9%88%D8%B7-%D8%B5%D8%AF%D8%B1-%D8%AA%D8%AC%D9%84%D9%8A%D8%AE-%D8%B3%D9%83%D8%B3-%D8%B9%D8%B1%D8%A7%D9%82%D9%8A.html" rel="dofollow">مقاطع تجليخ صدر عراقي</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%AE%D9%8A%D8%A7%D9%86%D9%87-%D8%B2%D9%88%D8%AC%D9%8A%D9%87-%D9%8A%D9%86%D9%8A%D9%83-%D9%85%D8%B1%D8%AA-%D8%A7%D8%AE%D9%88%D9%87.html" rel="dofollow">خيانة زوجية مرت اخوه</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%B9%D9%85%D8%A7%D9%86%D9%8A%D9%87-%D8%A7%D8%A8%D9%8A%D8%B6-%D9%85%D8%A7%D8%B2%D9%88%D8%AE%D9%8A%D9%87-%D9%85%D8%AD%D8%AC%D8%A8%D8%A9-xxarxx-%D8%AF%D9%8A%D9%88%D8%AF-%D9%8A%D9%85%D9%86%D9%8A%D9%87.html" rel="dofollow">يمنية بيضاء مازوخية</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%B3%D8%A7%D8%AF%D9%8A%D9%87-%D8%B3%D9%83%D8%B3-%D8%A7%D9%86%D8%AC%D9%8I-%D8%AE%D9%88%D8%B1%D9%8A-%D9%83%D8%B1%D8%AA%D9%88%D9%86-%D8%B3%D9%83%D8%B3.html" rel="dofollow">انجي خوري سادية كرتون</a> | 
        <a href="https://www.pjh.is/jri/ify/anal-%D9%85%D8%B5%D8%B1%D9%8A%D9%8A%D9%86-%D9%81%D8%A7%D8%AC%D8%B1-%D9%86%D9%8A%D9%83-%D8%B7%D9%8A%D8%B2-%D9%85%D8%AD%D8%AC%D8%A8%D8%A9-%D9%8A%D9%85%D9%86%D9%8A%D9%87-%D9%86%D9%8I%D9%83-%D8%AE%D9%84%D9%81%D9%8I.html" rel="dofollow">نيك خلفي محجبة يمنية</a> | 
        <a href="https://www.pjh.is/jri/ify/gore-adult-movie-guro-rimjob-hump-virgin-cameltoe.html" rel="dofollow">Gore Adult Movie Clips</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%AA%D8%A8%D8%A7%D8%AF%D9%84-%D8%B2%D9%88%D8%AC%D8%A7%D8%AA-%D9%8A%D9%85%D9%86%D9%8A%D9%87-%D9%85%D8%A7%D8%B2%D9%88%D8%AE%D9%8A%D9%87-%D8%B3%D9%88%D8%B1%D9%8A.html" rel="dofollow">تبادل زوجات يمنية وسوري</a> | 
        <a href="https://www.pjh.is/jri/ify/%D8%B3%D9%83%D8%B3-%D9%85%D8%B5%D8%B1%D9%8A-%D8%AC%D8%AF%D9%8A%D8%AF-%D9%81%D9%8A%D8%AF%D9%8A%D9%88-%D9%83%D8%A7%D9%85%D9%84.html" rel="dofollow">فيديو سكس مصري كامل</a> | 
        <a href="https://www.pjh.is/jri/ify/%D9%85%D8%B5%D8%B1%D9%8A-%D8%B3%D9%83%D8%B3-%D9%85%D8%B5%D8%B1%D9%8A-%D8%AC%D8%A7%D9%85%D8%AF-%D9%83%D8%B3-%D9%85%D8%B4%D8%A7%D9%87%D9%8A%D8%B1-%D9%85%D8%AA%D8%B9%D9%87.html" rel="dofollow">سكس مشاهير مصر متعة</a> | 
        <a href="https://www.pjh.is/jri/ify/%D9%85%D8%B1%D8%A7%D9%87%D9%82%D9%87-%D8%B3%D9%83%D8%B3-%D9%87%D9%86%D8%AA%D8%A7%D9%8A-%D9%81%D8%B6%D8%A7%D9%8A%D8%AD-%D9%85%D8%BA%D8%B1%D8%A8-%D8%B5%D8%AF%D8%B1-%D9%83%D8%A8%D9%8A%D8%B1-%D9%86%D9%88%D8%AF%D8%B2.html" rel="dofollow">فضايح نودز مغربية مراهقة</a> | 
        <a href="https://www.pjh.is/jri/ify/deap-throating-anal-menstrual-cum-shot-naked-dick-black.html" rel="dofollow">Black Dick Deep Throat Anal</a>
    </p>
</footer>
"""

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # منع التكرار وإضافة الروابط قبل إغلاق وسم body
            if "www.pjh.is" not in content and "</body>" in content:
                new_content = content.replace("</body>", f"{links_to_inject}</body>")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Done: {path}")
