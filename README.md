# NetPulse v1.0

**RHEL 10 Network Diagnostic & Troubleshooting Tool**

NetPulse is a modular Python-based network diagnostic tool designed for RHEL 10 and Linux systems. It checks network interfaces, routing, DNS, internet connectivity, TCP ports, and generates an overall network health score with diagnostic status and recommendations.

## Features

- Network interface information
- Interface status, IP address and subnet detection
- Default gateway detection
- Route reachability and latency testing
- DNS resolver and DNS resolution testing
- Internet connectivity testing
- Latency measurement
- Packet-loss detection
- TCP port checking
- Automated network health scoring
- HEALTHY, WARNING and CRITICAL status
- Diagnostic recommendations
- Graceful handling of command failures and timeouts
- RHEL 10 compatible
- Python 3 standard library only
- No external pip packages required

## Architecture

```text
NetPulse/
├── netpulse.py       Main controller
├── interface.py      Network interface information
├── routing.py        Gateway, route and latency checks
├── dns.py            DNS resolver and resolution checks
├── connectivity.py   Internet connectivity, latency and packet loss
├── ports.py          TCP port state checks
├── diagnosis.py      Health score and recommendations
├── README.md         Project documentation
└── screenshots/      Sample execution screenshots
## How It Works

1. Detects the active network interface.
2. Collects IP address and subnet information.
3. Detects the default gateway.
4. Checks route reachability and latency.
5. Validates DNS resolver configuration.
6. Tests DNS resolution and response time.
7. Tests internet connectivity.
8. Measures latency and packet loss.
9. Checks selected TCP ports.
10. Calculates the overall network health score.
11. Displays diagnostic status and recommendations.

## Requirements

- RHEL 10 or compatible Linux distribution
- Python 3.9+
- Linux networking utilities such as `ip` and `ping`
- No external Python packages required

## Usage

Run NetPulse from the project directory:

```bash
python3 netpulse.py

Phir ye sections paste karo:

```markdown
## Technologies Used

- Python 3
- RHEL 10
- Linux
- TCP/IP Networking
- DNS
- Routing
- Socket Programming
- Subprocess
- Git
- GitHub
- SSH

## Scoring

| Level | Penalty |
|---|---:|
| WARNING | -8 |
| CRITICAL | -20 |
| UNKNOWN | -5 |

| Score | Status |
|---:|---|
| ≥ 85 | HEALTHY |
| 60–84 | WARNING |
| < 60 | CRITICAL |

## Sample Output

NetPulse running on RHEL 10:

![NetPulse Sample Output](screenshots/NetPulse_Output.png)

## Testing

The tool was tested on RHEL 10 with:

- Network interface detection
- Default gateway validation
- DNS resolution
- Internet connectivity
- Network latency
- Packet loss
- TCP port availability

Example successful execution:

```text
NETWORK SCORE : 100/100
STATUS        : HEALTHY

Phir ye sections paste karo:

```markdown
## Technologies Used

- Python 3
- RHEL 10
- Linux
- TCP/IP Networking
- DNS
- Routing
- Socket Programming
- Subprocess
- Git
- GitHub
- SSH

## Scoring

| Level | Penalty |
|---|---:|
| WARNING | -8 |
| CRITICAL | -20 |
| UNKNOWN | -5 |

| Score | Status |
|---:|---|
| ≥ 85 | HEALTHY |
| 60–84 | WARNING |
| < 60 | CRITICAL |

## Sample Output

NetPulse running on RHEL 10:

![NetPulse Sample Output](screenshots/NetPulse_Output.png)

## Testing

The tool was tested on RHEL 10 with:

- Network interface detection
- Default gateway validation
- DNS resolution
- Internet connectivity
- Network latency
- Packet loss
- TCP port availability

Example successful execution:

```text
NETWORK SCORE : 100/100
STATUS        : HEALTHY

Phir ye sections paste karo:

```markdown
## Technologies Used

- Python 3
- RHEL 10
- Linux
- TCP/IP Networking
- DNS
- Routing
- Socket Programming
- Subprocess
- Git
- GitHub
- SSH

## Scoring

| Level | Penalty |
|---|---:|
| WARNING | -8 |
| CRITICAL | -20 |
| UNKNOWN | -5 |

| Score | Status |
|---:|---|
| ≥ 85 | HEALTHY |
| 60–84 | WARNING |
| < 60 | CRITICAL |

## Sample Output

NetPulse running on RHEL 10:

![NetPulse Sample Output](screenshots/NetPulse_Output.png)

## Testing

The tool was tested on RHEL 10 with:

- Network interface detection
- Default gateway validation
- DNS resolution
- Internet connectivity
- Network latency
- Packet loss
- TCP port availability

Example successful execution:

```text
NETWORK SCORE : 100/100
STATUS        : HEALTHY
## Future Improvements

- Configurable TCP port lists
- JSON report generation
- Historical diagnostic reports
- Scheduled monitoring
- Optional email alerts
- Additional network protocol checks

## Project Goals

NetPulse is designed as a lightweight, dependency-free network troubleshooting tool for Linux administrators,
support engineers, and networking learners.
