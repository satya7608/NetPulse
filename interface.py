"""Network interface detection: name, status, IP, subnet mask."""
import subprocess
import ipaddress


def run_cmd(cmd, timeout=5):
    """Run a shell command safely and return its stdout, or '' on failure."""
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return r.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
        return ""


def get_default_iface():
    """Return the name of the interface used for the default route."""
    out = run_cmd(["ip", "route", "show", "default"])
    parts = out.split()
    if "dev" in parts:
        return parts[parts.index("dev") + 1]
    return None


def get_iface_status(iface):
    """Return UP or DOWN for the given interface."""
    out = run_cmd(["ip", "-o", "link", "show", iface])
    return "UP" if "state UP" in out else "DOWN"


def get_iface_ip(iface):
    """Return (ip, subnet_mask) for the given interface."""
    out = run_cmd(["ip", "-o", "-4", "addr", "show", iface])
    for token in out.split():
        if "/" in token and token[0].isdigit():
            try:
                net = ipaddress.ip_interface(token)
                return str(net.ip), str(net.netmask)
            except ValueError:
                continue
    return "unknown", "unknown"


def collect():
    """Collect all interface metrics into a single dictionary."""
    iface = get_default_iface() or "unknown"
    status = get_iface_status(iface) if iface != "unknown" else "DOWN"
    ip, subnet = get_iface_ip(iface) if iface != "unknown" else ("unknown", "unknown")
    return {"name": iface, "status": status, "ip": ip, "subnet": subnet}
