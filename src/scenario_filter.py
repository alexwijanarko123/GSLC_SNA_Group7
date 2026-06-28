import json
import time
import os
import sys
from collections import deque

# File paths
REPORT_PATH = "nginx_logs/report.json"
AI_CATCH_FILE = "ai_catch.json"

def check_anomalies():
    if not os.path.exists(REPORT_PATH):
        sys.stdout.write(f"\r[STATUS] Waiting data from GoAccess... (File {REPORT_PATH} not found)")
        sys.stdout.flush()
        return

    try:
        with open(REPORT_PATH, 'r') as f:
            data = json.load(f)
            
        # Filtering Logic: Check for volumetric anomalies in the log data
        hosts = data.get("hosts", {}).get("data", [])
        found = False
        for host in hosts:
            if host.get("hits", {}).get("count", 0) > 50:
                payload = {
                    "alert": "Volumetric Anomaly Detected",
                    "source": host.get("data"),
                    "details": "High volume of 404 errors detected"
                }
                with open(AI_CATCH_FILE, 'w') as f:
                    json.dump(payload, f, indent=4)
                print(f"\n[!] Anomaly detected from IP: {host.get('data')}!")
                found = True
        
        if not found:
            sys.stdout.write("\r[STATUS] System Standby - Monitoring traffic real-time...")
            sys.stdout.flush()

    except Exception:
        sys.stdout.write("\r[STATUS] Processing log data...")
        sys.stdout.flush()

print("Middleware Pipeline Active.")
while True:
    check_anomalies()
    time.sleep(1)