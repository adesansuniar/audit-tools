import re
import json
from pathlib import Path
from datetime import datetime

# ✅ Pemetaan status dan label
STATUS_MAP = {
    "✅": "Online",
    "❌": "404 Not Found",
    "⚠️": "Timeout / Error",
    "OK": "Online",
    "ERROR": "Timeout / Error"
}

# 🔎 Parsing log line dengan normalisasi spasi
def parse_log_line(line):
    line = re.sub(r'\s{2,}', ' ', line.strip())
    match = re.match(r'^(\S+)\s+(✅|❌|⚠️|OK|ERROR)\s+(.*)$', line)
    if match:
        return {
            "slug": match.group(1),
            "status": match.group(2),
            "label": STATUS_MAP.get(match.group(2), "Unknown"),
            "keterangan": match.group(3)
        }
    return None

# 🚦 Validasi slug (bisa diperluas ke prefix folder tertentu)
def is_valid_slug(slug):
    return re.match(r'^[\w\-/]+\.html$', slug) is not None

# 📄 Baca dan parsing log audit
def read_audit_log(log_path):
    entries = []
    if Path(log_path).is_file():
        with open(log_path, "r", encoding="utf-8") as f:
            for line in f:
                entry = parse_log_line(line)
                if entry and is_valid_slug(entry["slug"]):
                    entries.append(entry)
    return entries

# 📊 Rekap status keseluruhan
def summarize_status(entries):
    summary = {emoji: 0 for emoji in STATUS_MAP if emoji in ["✅", "❌", "⚠️"]}
    for e in entries:
        if e["status"] in summary:
            summary[e["status"]] += 1
    return summary

# 📦 Ekspor hasil audit ke JSON
def export_to_json(entries, path):
    result = {
        "audit_date": datetime.now().strftime("%Y-%m-%d"),
        "summary": summarize_status(entries),
        "details": entries
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
