from datetime import datetime
import json

result = {
    "audit_date": datetime.now().strftime("%Y-%m-%d"),
    "summary": {"ok": 0, "not_found": 0, "error": 0},
    "details": []
}

with open("audit/audit-log.txt") as log:
    for line in log:
        slug, status = line.strip().split(" ", 1)
        result["details"].append({"slug": slug, "status": status})
        if "✅" in status:
            result["summary"]["ok"] += 1
        elif "❌" in status:
            result["summary"]["not_found"] += 1
        else:
            result["summary"]["error"] += 1

with open("audit-result.json", "w") as out:
    json.dump(result, out, indent=2)
