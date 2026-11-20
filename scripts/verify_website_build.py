import os
import sys
import re

def verify_build():
    if not os.path.exists("index.html"):
        print("ERROR: index.html not found")
        sys.exit(1)
        
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    # Check KaTeX
    if "katex.min.css" not in html or "auto-render.min.js" not in html:
        print("ERROR: Missing KaTeX CSS or auto-render script")
        sys.exit(1)
        
    # Check Unslop (no generic AI purple/indigo gradient slop)
    slop_indicators = ["#8b5cf6", "#6366f1", "from-blue-400 to-purple-600"]
    for s in slop_indicators:
        if s.lower() in html.lower():
            print(f"ERROR: Found AI slop artifact '{s}' in index.html")
            sys.exit(1)
            
    # Check required interface components
    required_components = [
        "search-input",
        "theme-toggle",
        "pillar-tabs",
        "case-study-hub",
        "formula-sheet",
        "checkpoint"
    ]
    for comp in required_components:
        if comp not in html.lower():
            print(f"ERROR: Missing key UI element containing '{comp}'")
            sys.exit(1)
            
    print("WEBSITE_BUILD_VERIFIED: EDITORIAL_STANDARDS_MET")

if __name__ == "__main__":
    verify_build()
