with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

print("index.html length:", len(html))
print("endsem-qb-tab found:", 'id="endsem-qb-tab"' in html)
print("renderEndsemQuestionBank found:", "renderEndsemQuestionBank" in html)
print("KaTeX CSS found:", "katex.min.css" in html)
print("EQB questions count in DB:", html.count("EQB-"))
print("Classes covered in QB:")
for cid in range(11, 20):
    print(f"  Class {cid}: {html.count(f'EQB-{cid}-')} questions")
