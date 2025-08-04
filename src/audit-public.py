import os
import requests
import subprocess
from datetime import datetime
from urllib.parse import urljoin

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
TIMEOUT = 5

def cek_url_online(path):
    try:
        url = urljoin(BASE_URL, path)
        resp = requests.head(url, timeout=TIMEOUT)
        return resp.status_code
    except Exception as e:
        return f"ERROR: {str(e)}"

def path_exists(p): return os.path.exists(p)

def audit_slug_file(source_file, log_file):
    if not path_exists(source_file):
        print(f"❌ File tidak ditemukan: {source_file}")
        return []

    total_ok, total_404, total_err = 0, 0, 0
    hasil = []

    with open(source_file, "r") as f:
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

    with open(log_file, "w") as log:
        log.write("\n".join(hasil))

    print("\n".join(hasil))
    return hasil

def git_push(file_path):
    subprocess.run(["git", "add", file_path])
    subprocess.run(["git", "commit", "-m", f"Auto audit log {datetime.now().isoformat()}"])
    subprocess.run(["git", "push"])

def main():
    SOURCE_FILE = "daftar-public.txt"
    LOG_FILE = "hasil-public-log.txt"
    hasil = audit_slug_file(SOURCE_FILE, LOG_FILE)

    if hasil:  # Kalau hasil tidak kosong
        git_push(LOG_FILE)

if __name__ == "__main__":
    main()
