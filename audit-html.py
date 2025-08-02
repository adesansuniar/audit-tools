import requests
import os

BASE_URL = "https://adesansuniar.github.io/blog-adesansuniar/"
TIMEOUT = 5
DAFTAR_FILE = "daftar-html.txt"          # Karena berada di root repo
LOG_FILE = "audit/audit-log.txt"         # Hasil tetap disimpan di folder audit/

def cek_file_lokal(filepath):
    return os.path.exists(filepath)

def cek_url_online(slug):
    try:
        resp = requests.head(BASE_URL + slug, timeout=TIMEOUT)
        return resp.status_code
    except Exception as e:
        return f"ERROR: {str(e)}"

def audit():
    if not os.path.exists(DAFTAR_FILE):
        print(f"File {DAFTAR_FILE} tidak ditemukan.")
        return

    hasil_log = []

    with open(DAFTAR_FILE, "r") as f:
        baris_list = f.readlines()

    for baris in baris_list:
        if "|" not in baris:
            continue
        path, tipe = baris.strip().split("|")
        hasil = ""

        if tipe == "public":
            status = cek_url_online(path)
            hasil = f"🌐 {path} => {status}"
        elif tipe in ["includes", "layouts"]:
            status = cek_file_lokal(path)
            hasil = f"📁 {path} => {'ADA' if status else 'TIDAK ADA'}"
        else:
            hasil = f"❓ {path} => TIPE TIDAK DIKENAL"

        print(hasil)
        hasil_log.append(hasil)

    with open(LOG_FILE, "w") as log:
        log.write("\n".join(hasil_log))

if __name__ == "__main__":
    audit()
