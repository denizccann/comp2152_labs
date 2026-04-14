# ============================================================
#  WEEK 14 LAB — Q2: HTTP SECURITY HEADER CHECKER
#  COMP2152 — [Deniz Can]
# ============================================================

import urllib.request

# Security headers every website should have
REQUIRED_HEADERS = {
    "Content-Type":              "Defines the content format",
    "X-Frame-Options":           "Vulnerable to clickjacking",
    "X-Content-Type-Options":    "Vulnerable to MIME sniffing",
    "Strict-Transport-Security": "No HTTPS enforcement",
    "Content-Security-Policy":   "No XSS protection policy",
    "X-XSS-Protection":          "No XSS filter",
}

def check_headers(url):
    """Checks a URL for the presence of required security headers."""
    try:
        with urllib.request.urlopen(url) as response:
            headers = dict(response.headers)
            results = []
            
            for header_name in REQUIRED_HEADERS:
                if header_name in headers:
                    results.append({
                        "header": header_name, 
                        "present": True, 
                        "value": headers[header_name]
                    })
                else:
                    results.append({
                        "header": header_name, 
                        "present": False, 
                        "value": "MISSING"
                    })
            return results
    except Exception:
        return []

def generate_report(url, results):
    """Prints a formatted report of the security header check."""
    print(f"URL: {url}")
    missing_count = 0
    
    for item in results:
        header = item["header"]
        value = item["value"]
        
        if item["present"]:
            print(f"  ✓ {header}: {value}")
        else:
            print(f"  ✗ {header}: MISSING — {REQUIRED_HEADERS[header]}")
            missing_count += 1
            
    print(f"\n  Missing {missing_count} of {len(results)} security headers!")

# --- Main (provided) ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: HTTP SECURITY HEADER CHECKER")
    print("=" * 60)

    urls = [
        "http://httpbin.org",
        "https://www.google.com",
    ]

    for url in urls:
        print(f"\n--- Checking {url} ---")
        results = check_headers(url)
        if results:
            generate_report(url, results)
        else:
            print("  (could not connect or not implemented)")

    print("\n" + "=" * 60)