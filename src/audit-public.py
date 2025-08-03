import requests
from urllib.parse import urljoin

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
TIMEOUT = 5
SOURCE_FILE = "daftar-public.txt"
LOG_FILE = "hasil-public-log.txt"

def cek_url_online(path):
    try:
        url = urljoin(BASE_URL, path)
        resp = requests.head(url, timeout=TIMEOUT)
        return resp.status_code
    except Exception as e:
        return f"ERROR: {str(e)}"

def audit_public():
    if not path_exists(SOURCE_FILE):
        print(f"❌ File tidak ditemukan: {SOURCE_FILE}")
        return

    total_ok, total_404, total_err = 0, 0, 0
    hasil = []

    with open(SOURCE_FILE, "r") as f:
        for line in f:
            if "|" not in line:
                continue
            slug, tipe = line.strip().split("|")
            status = cek_url_online(slug)

            if status == 200:
                hasil.append(f"✅ {slug} → ONLINE")
                total_ok += 1
            elif status == 404:
                hasil.append(f"❌ {slug} → 404 Not Found")
                total_404 += 1
            else:
                hasil.append(f"⚠️ {slug} → {status}")
                total_err += 1

    hasil.append(f"\n🔎 REKAP: {total_ok} OK | {total_404} 404 | {total_err} Error")
    print("\n".join(hasil))

    with open(LOG_FILE, "w") as log:
        log.write("\n".join(hasil))

def path_exists(p): return os.path.exists(p)

if __name__ == "__main__":
    audit_public()
        
