import pypdf

pdf_path = "Lecture_Slides/Class-11-Climate Change-Technology Solutions.pdf"
reader = pypdf.PdfReader(pdf_path)

for i, page in enumerate(reader.pages):
    print(f"==================== SLIDE {i+1} ====================")
    text = page.extract_text()
    print(text.strip())
    print()
