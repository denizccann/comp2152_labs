# ============================================================
#  WEEK 13 LAB — Q2: ASCII DASHBOARD
#  COMP2152 — Deniz Can
# ============================================================

import csv

SAMPLE_FILE = "scan_results.csv"

def load_findings(filename):
    """CSV verilerini yükler."""
    try:
        with open(filename, "r") as f:
            return list(csv.DictReader(f))
    except FileNotFoundError:
        return []

def bar_chart(data, title, max_width=30):
    """Başlığı ve yatay ASCII bar grafiğini yazdırır."""
    print(title)
    if not data:
        return
    
    max_val = max(count for _, count in data)
    for label, count in data:
        # Uzunluğu en yüksek değere göre oranlayarak ölçeklendirir
        bar_length = int((count / max_val) * max_width)
        print(f"  {label:<15} {'█' * bar_length} {count}")

def severity_summary(findings):
    """Önem derecesine göre sayıları (HIGH, MEDIUM, LOW sırasıyla) döndürür."""
    counts = {}
    for f in findings:
        sev = f["severity"]
        counts[sev] = counts.get(sev, 0) + 1
    
    return [(s, counts.get(s, 0)) for s in ["HIGH", "MEDIUM", "LOW"]]

def timeline(findings):
    """Tarihe göre bulgu sayılarını sıralı bir şekilde döndürür."""
    counts = {}
    for f in findings:
        date = f["date"]
        counts[date] = counts.get(date, 0) + 1
    
    return sorted(counts.items())

if __name__ == "__main__":
    print("=" * 60)
    print("  Q2: ASCII DASHBOARD")
    print("=" * 60)

    findings = load_findings(SAMPLE_FILE)

    if findings:
        print()
        sev = severity_summary(findings)
        if sev:
            bar_chart(sev, "SEVERITY BREAKDOWN")

        print()
        dates = timeline(findings)
        if dates:
            bar_chart(dates, "FINDINGS BY DATE")

        print()
        type_counts = {}
        for f in findings:
            t = f["type"]
            type_counts[t] = type_counts.get(t, 0) + 1
        type_data = sorted(type_counts.items(), key=lambda x: x[1], reverse=True)
        if type_data:
            bar_chart(type_data, "VULNERABILITY TYPES")
    else:
        print("\n  (Lütfen önce Q1 dosyasını çalıştırarak veriyi oluşturun)")

    print("\n" + "=" * 60)