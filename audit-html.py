import requests
from datetime import datetime

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
INPUT_FILE = "audit/daftar-html.txt"
OUTPUT_LOG = "audit/audit-log.txt"

def cek_url(slug):
    url = BASE_URL + slug
    try:
        r = requests.head(url, timeout=5)
        return f"{r.status_code} OK" if r.status_code == 200 else f"{r.status_code} ERROR"
    except Exception as e:
        return f"ERROR: {str(e)}"

def audit():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        slugs = [line.strip() for line in f if line.strip()]

    hasil = []
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = f"AUDIT HTML - {timestamp}\n{'-'*50}"
    hasil.append(header)
    print(header)

    for slug in slugs:
        status = cek_url(slug)
        baris = f"{slug:<35} => {status}"
        hasil.append(baris)
        print(baris)

    with open(OUTPUT_LOG, "w", encoding="utf-8") as f:
        f.write("\n".join(hasil))

    print(f"\n✅ Hasil audit tersimpan di: {OUTPUT_LOG}")

if __name__ == "__main__":
    audit()
