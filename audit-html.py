import requests
import os

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
EXT = ".html"
TIMEOUT = 5

def cek_file(slug):
    """Cek apakah file HTML tersedia secara online."""
    try:
        resp = requests.head(f"{BASE_URL}{slug}{EXT}", timeout=TIMEOUT)
        return resp.status_code
    except Exception as e:
        return f"ERROR: {str(e)}"

def audit(file_list_path="audit/daftar-html.txt", log_file_path="audit/audit-log.txt"):
    if not os.path.exists(file_list_path):
        print(f"[!] File list tidak ditemukan: {file_list_path}")
        return

    with open(file_list_path, "r") as f:
        slugs = [line.strip() for line in f if line.strip()]

    log_lines = []
    for slug in slugs:
        status = cek_file(slug)
        log_lines.append(f"{slug}{EXT}: {status}")
        print(f"🔎 {slug}{EXT} => {status}")

    with open(log_file_path, "w") as f:
        f.write("\n".join(log_lines))
    print(f"\n✅ Audit selesai. Hasil disimpan ke {log_file_path}")

if __name__ == "__main__":
    audit()
