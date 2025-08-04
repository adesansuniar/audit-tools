import os
import subprocess
from datetime import datetime

SOURCE_FILE = "daftar-internal.txt"
LOG_FILE = "hasil-internal-log.txt"

def audit_internal():
    if not os.path.exists(SOURCE_FILE):
        print(f"❌ File tidak ditemukan: {SOURCE_FILE}")
        return

    total_ada, total_tidak = 0, 0
    hasil = []

    with open(SOURCE_FILE, "r") as f:
        for line in f:
            if "|" not in line:
                continue
            path, tipe = line.strip().split("|")
            exists = os.path.exists(path)

            if exists:
                hasil.append(f"📁 {path} → ADA")
                total_ada += 1
            else:
                hasil.append(f"🚫 {path} → TIDAK DITEMUKAN")
                total_tidak += 1

    hasil.append(f"\n🧮 REKAP: {total_ada} Ada | {total_tidak} Hilang")
    print("\n".join(hasil))

    with open(LOG_FILE, "w") as log:
        log.write("\n".join(hasil))

    # 🚀 Commit & Push ke GitHub
    subprocess.run(["git", "add", LOG_FILE])
    subprocess.run(["git", "commit", "-m", f"Audit internal log {datetime.now().isoformat()}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    audit_internal()
