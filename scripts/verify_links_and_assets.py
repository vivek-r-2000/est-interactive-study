import os
import sys
import re

def verify_assets():
    if not os.path.exists("index.html"):
        print("ERROR: index.html not found")
        sys.exit(1)
        
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
        
    if "</html>" not in html or "</body>" not in html:
        print("ERROR: Malformed HTML in index.html")
        sys.exit(1)
        
    # Check that referenced local files in index.html exist
    local_srcs = re.findall(r'(?:src|href)=["\'](?!http|https|#|data:)([^"\']+)["\']', html)
    for src in local_srcs:
        # Strip query parameters if any
        clean_src = src.split('?')[0].split('#')[0]
        if clean_src and not os.path.exists(clean_src):
            print(f"ERROR: Broken local reference: {clean_src}")
            sys.exit(1)
            
    print("ASSET_INTEGRITY_VERIFIED: 0_BROKEN_LINKS")

if __name__ == "__main__":
    verify_assets()
