import os
import glob
import re

terms_by_class = {
    12: ["eia", "impact assessment", "great nicobar", "eac", "screening", "scoping", "public hearing"],
    13: ["bishnoi", "chipko", "appiko", "silent valley", "amrita devi", "sunderlal bahuguna", "gaura devi", "kssp"],
    14: ["green computing", "thin client", "thick client", "pue", "e-waste", "datacentre", "ict"],
    15: ["green engineering", "industrial ecology", "kalundborg", "denim", "life cycle assessment", "lca", "symbiosis"],
    16: ["seea", "sna", "green accounting", "natural capital", "depreciation", "gdp"],
    17: ["sdg", "sustainable development goal", "kuznets", "decoupling", "millennium"],
    18: ["natural resource accounting", "remote sensing", "gis", "geospatial"],
    19: ["anthropocentrism", "biocentrism", "ecocentrism", "land ethic", "ethics", "ramsar", "wetland", "kolkata wetland"]
}

files = glob.glob("Previous_Exam_Papers/extracted_questions/*.txt")
files.append("Previous_Exam_Papers/QUESTION_BANK_MASTER.md")

for cid, terms in terms_by_class.items():
    found = []
    for fpath in files:
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read().lower()
        for t in terms:
            if t in content:
                found.append(t)
    print(f"Class {cid}: matched search terms {list(set(found))}")
