"""Analyze collected network data and produce a diagnosis."""

THRESHOLDS = {
    "gw_latency_warn": 50, "gw_latency_crit": 150,
    "inet_latency_warn": 150, "inet_latency_crit": 400,
    "loss_warn": 5, "loss_crit": 20,
    "dns_warn": 100, "dns_crit": 300,
}
PENALTY = {"WARNING": 8, "CRITICAL": 20, "UNKNOWN": 5}


def level(value, warn, crit):
    """Classify a numeric value against warning/critical thresholds."""
    if value is None:
        return "UNKNOWN"
    if value >= crit:
        return "CRITICAL"
    if value >= warn:
        return "WARNING"
    return "HEALTHY"


def diagnose_interface(iface):
    """Evaluate interface up/down and IP assignment."""
    ok = iface["status"] == "UP" and iface["ip"] != "unknown"
    return {"status": "HEALTHY" if ok else "CRITICAL"}


def diagnose_routing(routing):
    """Evaluate default route reachability and latency."""
    if not routing["route_ok"]:
        return {"status": "CRITICAL", "issues": ["Default gateway unreachable"]}
    lvl = level(routing["latency_ms"], THRESHOLDS["gw_latency_warn"], THRESHOLDS["gw_latency_crit"])
    issues = [f"High gateway latency: {routing['latency_ms']}ms"] if lvl != "HEALTHY" else []
    return {"status": lvl, "issues": issues}


def diagnose_dns(dns):
    """Evaluate DNS resolver config and resolution performance."""
    issues = []
    if not dns["resolver_ok"]:
        issues.append("No DNS resolver configured")
    if not dns["resolution_ok"]:
        issues.append("DNS resolution failing")
    lvl = level(dns["response_ms"], THRESHOLDS["dns_warn"], THRESHOLDS["dns_crit"])
    if lvl not in ("HEALTHY", "UNKNOWN"):
        issues.append(f"Slow DNS response: {dns['response_ms']}ms")
    status = "CRITICAL" if not dns["resolution_ok"] else lvl
    return {"status": status, "issues": issues}


def diagnose_connectivity(conn):
    """Evaluate internet reachability, latency, and packet loss."""
    if not conn["connected"]:
        return {"status": "CRITICAL", "issues": ["No internet connectivity"]}
    issues = []
    lat_lvl = level(conn["latency_ms"], THRESHOLDS["inet_latency_warn"], THRESHOLDS["inet_latency_crit"])
    loss_lvl = level(conn["packet_loss"], THRESHOLDS["loss_warn"], THRESHOLDS["loss_crit"])
    if lat_lvl != "HEALTHY":
        issues.append(f"High latency: {conn['latency_ms']}ms")
    if loss_lvl != "HEALTHY":
        issues.append(f"Packet loss: {conn['packet_loss']}%")
    status = "CRITICAL" if "CRITICAL" in (lat_lvl, loss_lvl) else "WARNING" if issues else "HEALTHY"
    return {"status": status, "issues": issues}


def compute_score(*results):
    """Compute an overall network score out of 100 from a set of results."""
    score = 100
    for r in results:
        score -= PENALTY.get(r["status"], 0)
    return max(0, min(100, score))


def analyze(data):
    """Run the full diagnostic analysis over collected network data."""
    iface_r = diagnose_interface(data["interface"])
    routing_r = diagnose_routing(data["routing"])
    dns_r = diagnose_dns(data["dns"])
    conn_r = diagnose_connectivity(data["connectivity"])
    score = compute_score(iface_r, routing_r, dns_r, conn_r)
    overall = "CRITICAL" if score < 60 else "WARNING" if score < 85 else "HEALTHY"
    recs = routing_r.get("issues", []) + dns_r.get("issues", []) + conn_r.get("issues", [])
    if iface_r["status"] != "HEALTHY":
        recs.insert(0, "Check network interface cable/driver")
    return {
        "interface": iface_r, "routing": routing_r, "dns": dns_r, "connectivity": conn_r,
        "score": score, "overall_status": overall, "recommendations": recs,
    }
