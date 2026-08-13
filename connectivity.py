"""Internet connectivity: reachability, latency, packet loss."""
from interface import run_cmd


def ping_host(host="8.8.8.8", count=5):
    """Ping a host and return (avg_latency_ms, packet_loss_percent)."""
    out = run_cmd(["ping", "-c", str(count), "-W", "1", host], timeout=count * 2)
    times = [float(l.split("time=")[1].split()[0]) for l in out.splitlines() if "time=" in l]
    loss = 100.0
    for line in out.splitlines():
        if "packet loss" in line:
            try:
                loss = float(line.split("%")[0].split()[-1])
            except (IndexError, ValueError):
                pass
    latency = round(sum(times) / len(times), 1) if times else None
    return latency, loss


def collect():
    """Collect connectivity metrics into a single dictionary."""
    latency, loss = ping_host()
    return {"connected": latency is not None, "latency_ms": latency, "packet_loss": loss}
