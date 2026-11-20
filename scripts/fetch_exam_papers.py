import os
import urllib.request
import json
import pypdf

DEST_PDF_DIR = "Previous_Exam_Papers/pdfs"
DEST_TXT_DIR = "Previous_Exam_Papers/extracted_questions"
os.makedirs(DEST_PDF_DIR, exist_ok=True)
os.makedirs(DEST_TXT_DIR, exist_ok=True)

api_url = "https://api.github.com/repos/VijayrajS/iiitprevpapers/contents/Electives/CsFree/EVS-Environmental%20Science"
req = urllib.request.Request(api_url, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(req) as resp:
    files = json.loads(resp.read().decode("utf-8"))

print(f"Found {len(files)} files on GitHub.")

all_papers_summary = []

for f in files:
    name = f["name"]
    download_url = f.get("download_url")
    if not download_url or not name.endswith(".pdf"):
        continue

    pdf_path = os.path.join(DEST_PDF_DIR, name)
    txt_path = os.path.join(DEST_TXT_DIR, name.replace(".pdf", ".txt"))

    print(f"Downloading {name}...")
    dl_req = urllib.request.Request(download_url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(dl_req) as dl_resp:
        content = dl_resp.read()
        with open(pdf_path, "wb") as out_pdf:
            out_pdf.write(content)

    # Extract text using pypdf
    try:
        reader = pypdf.PdfReader(pdf_path)
        extracted_text = []
        for idx, page in enumerate(reader.pages):
            p_text = page.extract_text() or ""
            extracted_text.append(f"--- PAGE {idx+1} ---\n{p_text}")
        full_text = "\n\n".join(extracted_text)
    except Exception as e:
        full_text = f"Error extracting text: {e}"

    with open(txt_path, "w", encoding="utf-8") as out_txt:
        out_txt.write(full_text)

    char_count = len(full_text.strip())
    print(f"Saved {name}: {len(reader.pages) if 'reader' in locals() else 0} pages, {char_count} chars -> {txt_path}")
    all_papers_summary.append({
        "file": name,
        "txt_path": txt_path,
        "char_count": char_count
    })

# Also write a combined master file
master_txt_path = os.path.join(DEST_TXT_DIR, "ALL_PREVIOUS_EXAM_QUESTIONS.txt")
with open(master_txt_path, "w", encoding="utf-8") as master_out:
    for item in all_papers_summary:
        master_out.write(f"\n{'='*70}\n")
        master_out.write(f"EXAM PAPER: {item['file']}\n")
        master_out.write(f"{'='*70}\n\n")
        with open(item["txt_path"], "r", encoding="utf-8") as f_in:
            master_out.write(f_in.read())
            master_out.write("\n\n")

print(f"\nAll papers processed. Master corpus saved to {master_txt_path}")
