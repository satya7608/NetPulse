# NetPulse v1.0

RHEL 10 network diagnostic & troubleshooting tool, in pure Python 3
standard library (no external dependencies).

## Architecture

```
netpulse.py        Main controller — orchestrates checks & prints the report
├── interface.py     Default interface: name, status, IP, subnet mask
├── routing.py        Default gateway + latency + reachability
├── dns.py             Resolver config, resolution success, response time
├── connectivity.py   Internet reachability, latency, packet loss
├── ports.py           TCP port state check (22, 80, 443 by default)
└── diagnosis.py       Threshold analysis, network score, recommendations
```

All modules share one `run_cmd()` helper (defined in `interface.py`) that
wraps `subprocess` and never raises — missing commands or timeouts just
return an empty result, so the tool degrades gracefully.

## Requirements

- RHEL 10 (or any Linux with `ip`, `ping`, `cat /etc/resolv.conf`)
- Python 3.9+ — **no pip packages needed**

## Usage

```bash
python3 netpulse.py
```

Exit code is `2` if overall status is CRITICAL, otherwise `0` — safe to use
in cron/monitoring pipelines.

## Scoring

| Level    | Penalty |
|----------|---------|
| WARNING  | -8      |
| CRITICAL | -20     |
| UNKNOWN  | -5      |

| Score  | Status   |
|--------|----------|
| ≥ 85   | HEALTHY  |
| 60-84  | WARNING  |
| < 60   | CRITICAL |
