import json
import os
import re
import sys
import time

REPORT_PATH = "nginx_logs/report.json"
ACCESS_LOG_PATH = "nginx_logs/access.log"
AI_CATCH_FILE = "ai_catch.json"
ANOMALY_THRESHOLD = 50

LOG_LINE_PATTERN = re.compile(
    r'^(?P<ip>\S+) - - \[(?P<timestamp>[^\]]+)\] '
    r'"(?P<method>\S+) (?P<path>\S+) (?P<protocol>[^"]+)" '
    r'(?P<status>\d{3}) (?P<size>\S+) "(?P<referrer>[^"]*)" '
    r'"(?P<user_agent>[^"]*)" (?P<request_time>[\d.]+)$'
)


def parse_access_log_line(line):
    match = LOG_LINE_PATTERN.match(line.strip())
    if not match:
        return None

    entry = match.groupdict()
    entry["status"] = int(entry["status"])
    return entry


def load_access_log_entries():
    if not os.path.exists(ACCESS_LOG_PATH):
        return []

    entries = []
    with open(ACCESS_LOG_PATH, "r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            parsed = parse_access_log_line(line)
            if parsed:
                parsed["raw"] = line.rstrip("\n")
                entries.append(parsed)
    return entries


def build_payload(source_ip, offending_log_line, context_blocks):
    return {
        "alert": "Volumetric Anomaly Detected",
        "source": source_ip,
        "details": "High volume of 404 errors detected",
        "offending_log": offending_log_line,
        "context": context_blocks,
    }


def check_anomalies():
    if not os.path.exists(REPORT_PATH):
        sys.stdout.write(
            f"\r[STATUS] Waiting data from GoAccess... (File {REPORT_PATH} not found)"
        )
        sys.stdout.flush()
        return

    try:
        with open(REPORT_PATH, "r", encoding="utf-8") as report_file:
            report = json.load(report_file)

        access_entries = load_access_log_entries()
        hosts = report.get("hosts", {}).get("data", [])

        for host in hosts:
            if host.get("hits", {}).get("count", 0) <= ANOMALY_THRESHOLD:
                continue

            source_ip = host.get("data")

            # Isolate the IP's 404s specifically
            ip_404s = [
                entry
                for entry in access_entries
                if entry.get("ip") == source_ip and entry.get("status") == 404
            ]

            if not ip_404s:
                continue

            # Grab the latest 404 recorded as the representative trigger
            trigger_log = ip_404s[-1]["raw"]

            # Grab all general traffic for this IP for the context window
            all_ip_logs = [
                entry["raw"]
                for entry in access_entries
                if entry.get("ip") == source_ip and "raw" in entry
            ]

            context_blocks = [{"logs": all_ip_logs}]
            payload = build_payload(source_ip, trigger_log, context_blocks)

            print(f"\n[!] Anomaly detected from IP: {source_ip}!")

            with open(AI_CATCH_FILE, "w", encoding="utf-8") as output_file:
                json.dump(payload, output_file, indent=4)

            return 

        sys.stdout.write("\r[STATUS] System Standby - Monitoring traffic real-time...")
        sys.stdout.flush()

    except Exception:
        sys.stdout.write("\r[STATUS] Processing log data...")
        sys.stdout.flush()


def main():
    print("Middleware Pipeline Active.")
    while True:
        check_anomalies()
        time.sleep(1)


if __name__ == "__main__":
    main()