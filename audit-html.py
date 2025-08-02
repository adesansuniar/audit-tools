import requests
import os

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
TIMEOUT = 5

def cek_url(slug):
    try:
        url = f"{BASE_URL}{slug}"  # Tidak perlu tambah .html
        resp = requests.head(url, timeout=TIMEOUT)
        return resp.status_code
    except Exception as e:
        return f"ERROR: {str(e)}"

def audit(file_list="daftar-html.txt", log_file="audit-log.txt"):
    if not os.path.exists(file_list):
        print(f"❌ File daftar tidak ditemukan: {file_list}")
        return

    with open(file_list, "r") as f:
        slugs = [line.strip() for line in f if line.strip()]

    with open(log_file, "w") as out:
        for slug in slugs:
            status = cek_url(slug)
            log_line = f"🔎 {slug} => {status}"
            print(log_line)
            out.write(log_line + "\n")

if __name__ == "__main__":
    audit()
