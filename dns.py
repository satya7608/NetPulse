"""DNS resolver configuration and resolution diagnostics."""
import socket
import time
from interface import run_cmd


def get_resolver():
    """Return the first configured nameserver from /etc/resolv.conf."""
    out = run_cmd(["cat", "/etc/resolv.conf"])
    for line in out.splitlines():
        if line.strip().startswith("nameserver"):
            return line.split()[1]
    return "unknown"


def resolve(host="google.com"):
    """Resolve a hostname and return (success, response_time_ms)."""
    start = time.time()
    try:
        socket.gethostbyname(host)
        return True, round((time.time() - start) * 1000, 1)
    except socket.gaierror:
        return False, None


def collect():
    """Collect all DNS metrics into a single dictionary."""
    resolver = get_resolver()
    ok, response_ms = resolve()
    return {
        "resolver": resolver,
        "resolver_ok": resolver != "unknown",
        "resolution_ok": ok,
        "response_ms": response_ms,
    }
