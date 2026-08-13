"""Port reachability checks on the local host."""
import socket

DEFAULT_PORTS = [22, 80, 443]


def check_port(port, host="127.0.0.1", timeout=1):
    """Return True if the given TCP port is open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            return s.connect_ex((host, port)) == 0
    except OSError:
        return False


def collect(ports=None):
    """Check a list of ports and return their OPEN/CLOSED state."""
    ports = ports or DEFAULT_PORTS
    return {p: ("OPEN" if check_port(p) else "CLOSED") for p in ports}
