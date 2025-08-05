import os
from src import utils  # Pastikan struktur repo kamu sudah pakai src/

LOG_FILE = "audit/audit-log.txt"
REKAP_FILE = "audit/audit-rekap.md"

def generate_markdown_table(entries):
    header = "| File | Status |\n|------|--------|\n"
    rows = []
    for e in entries:
        status_icon = utils.status_label(e["status"])
        rows.append(f"| {e['slug']} | {e['status']} {status_icon} |")
    return header + "\n".join(rows)

def generate_summary_line(summary_dict):
    return f"**Rekap:** ✅ {summary_dict.get('✅',0)} | ❌ {summary_dict.get('❌',0)} | ⚠️ {summary_dict.get('⚠️',0)}**\n"

def main():
    os.makedirs(os.path.dirname(REKAP_FILE), exist_ok=True)

    entries = utils.read_audit_log(LOG_FILE)
    if not entries:
        print("⚠️ Tidak ada log valid untuk diproses.")
        return

    markdown = "# 🔍 Rekap Audit HTML\n\n"
    markdown += generate_markdown_table(entries) + "\n\n"
    markdown += generate_summary_line(utils.summarize_status(entries))

    with open(REKAP_FILE, "w", encoding="utf-8") as f:
        f.write(markdown)

    print(f"✅ Rekap Markdown berhasil dibuat: {REKAP_FILE}")

if __name__ == "__main__":
    main()
