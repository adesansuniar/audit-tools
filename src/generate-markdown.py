import os
from src import utils  # pastikan struktur repo kamu sudah pakai src/

LOG_FILE = "audit/audit-log.txt"
REKAP_FILE = "audit/audit-rekap.md"

def generate_markdown_table(entries):
    header = "| File | Status |\n|------|--------|\n"
    rows = "\n".join(f"| {e['slug']} | {e['status']} {utils.status_label(e['status'])} |" for e in entries)
    return header + rows

def main():
    # Pastikan folder audit tersedia
    os.makedirs("audit", exist_ok=True)

    entries = utils.read_audit_log(LOG_FILE)
    if not entries:
        print("⚠️ Tidak ada log valid untuk diproses.")
        return

    markdown = "# 🔍 Rekap Audit HTML\n\n" + generate_markdown_table(entries) + "\n\n"
    summary = utils.summarize_status(entries)
    markdown += f"**Rekap:** ✅ {summary['✅']} | ❌ {summary['❌']} | ⚠️ {summary['⚠️']}\n"

    with open(REKAP_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Rekap Markdown berhasil dibuat: {REKAP_FILE}")

if __name__ == "__main__":
    main()
