from utils import read_audit_log, export_to_json

LOG_PATH = "audit/audit-log.txt"
OUTPUT_PATH = "audit/audit-result.json"

entries = read_audit_log(LOG_PATH)
if not entries:
    print("⚠️ Audit log kosong atau tidak valid.")
else:
    export_to_json(entries, OUTPUT_PATH)
    print(f"✅ File JSON berhasil dibuat: {OUTPUT_PATH}")
