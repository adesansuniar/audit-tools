import re
from pathlib import Path

# 🔎 Validasi dan parsing log line
def parse_log_line(line):
    # Format: nama_file STATUS KETERANGAN
    match = re.match(r'^(\S+)\s+(✅|❌|⚠️)\s+(.*)$', line.strip())
    if match:
        return {
            "slug": match.group(1),
            "status": match.group(2),
            "keterangan": match.group(3)
        }
    return None

# 🔁 Konversi emoji ke label status
def status_label(code):
    return {
        "✅": "Online",
        "❌": "404 Not Found",
        "⚠️": "Timeout / Error"
    }.get(code, "Unknown")

# 🚦 Filter hanya slug yang valid
def is_valid_slug(slug):
    return re.match(r'^[\w\-/]+\.html$', slug) is not None

# 📄 Baca file log dan parsing seluruh isi
def read_audit_log(log_path):
    entries = []
    if Path(log_path).is_file():
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = parse_log_line(line)
                if entry and is_valid_slug(entry["slug"]):
                    entries.append(entry)
    return entries

# 🧮 Rekap statistik status
def summarize_status(entries):
    summary = {"✅": 0, "❌": 0, "⚠️": 0}
    for e in entries:
        if e["status"] in summary:
            summary[e["status"]] += 1
    return summary
