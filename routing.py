"""Routing diagnostics: default gateway and reachability."""
from interface import run_cmd


def get_gateway():
    """Return the default gateway IP address."""
    out = run_cmd(["ip", "route", "show", "default"])
    parts = out.split()
    if "via" in parts:
        return parts[parts.index("via") + 1]
    return "unknown"


def ping_gateway(gateway, count=2):
    """Ping the gateway and return average round-trip time in ms, or None."""
    if gateway == "unknown":
        return None
    out = run_cmd(["ping", "-c", str(count), "-W", "1", gateway], timeout=count * 2)
    times = [float(l.split("time=")[1].split()[0]) for l in out.splitlines() if "time=" in l]
    return round(sum(times) / len(times), 1) if times else None


def collect():
    """Collect gateway and route reachability into a single dictionary."""
    gateway = get_gateway()
    latency = ping_gateway(gateway)
    return {"gateway": gateway, "latency_ms": latency, "route_ok": latency is not None}
