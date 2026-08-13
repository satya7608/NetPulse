#!/usr/bin/env python3
"""NetPulse v1.0 - RHEL 10 Network Diagnostic & Troubleshooting Tool."""
import sys

import interface
import routing
import dns
import connectivity
import ports
import diagnosis

CHECK, CROSS = "\u2713", "\u2717"


def mark(status):
    return {"HEALTHY": CHECK, "WARNING": "!", "CRITICAL": CROSS, "UNKNOWN": "?"}.get(status, "?")


def print_report(data, diag):
    i, r, d = data["interface"], data["routing"], data["dns"]
    c, p = data["connectivity"], data["ports"]

    print("INTERFACE")
    print(f"Name        : {i['name']}")
    print(f"Status      : {i['status']}")
    print(f"IP          : {i['ip']}")
    print(f"Subnet      : {i['subnet']}")

    print("\nROUTING")
    print(f"Gateway     : {r['gateway']}")
    print(f"Latency     : {r['latency_ms']} ms" if r["latency_ms"] is not None else "Latency     : N/A")
    print(f"Route       : {'OK' if r['route_ok'] else 'FAIL'} {mark(diag['routing']['status'])}")

    print("\nDNS")
    print(f"Resolver    : {'OK' if d['resolver_ok'] else 'FAIL'} {mark('HEALTHY' if d['resolver_ok'] else 'CRITICAL')}")
    print(f"Resolution  : {'SUCCESS' if d['resolution_ok'] else 'FAILED'} {mark('HEALTHY' if d['resolution_ok'] else 'CRITICAL')}")
    print(f"Response    : {d['response_ms']} ms" if d["response_ms"] is not None else "Response    : N/A")

    print("\nCONNECTIVITY")
    print(f"Internet    : {'CONNECTED' if c['connected'] else 'DISCONNECTED'} {mark(diag['connectivity']['status'])}")
    print(f"Latency     : {c['latency_ms']} ms" if c["latency_ms"] is not None else "Latency     : N/A")
    print(f"Packet Loss : {c['packet_loss']}%")

    print("\nPORTS")
    for port, state in p.items():
        print(f"{port:<12}: {state}")

    print("\nDIAGNOSIS")
    print(f"Interface   : {diag['interface']['status']}")
    print(f"Routing     : {diag['routing']['status']}")
    print(f"DNS         : {diag['dns']['status']}")
    print(f"Internet    : {diag['connectivity']['status']}")
    print(f"NETWORK SCORE : {diag['score']}/100")
    print(f"STATUS        : {diag['overall_status']}")

    print("\nRECOMMENDATION")
    if diag["recommendations"]:
        for rec in diag["recommendations"]:
            print(f"- {rec}")
    else:
        print("None")


def main():
    print("=" * 50)
    print(" NETPULSE v1.0")
    print(" RHEL 10 Network Diagnostic & Troubleshooting Tool")
    print("=" * 50)

    data = {
        "interface": interface.collect(),
        "routing": routing.collect(),
        "dns": dns.collect(),
        "connectivity": connectivity.collect(),
        "ports": ports.collect(),
    }
    diag = diagnosis.analyze(data)
    print_report(data, diag)
    print("=" * 50)
    sys.exit(0 if diag["overall_status"] != "CRITICAL" else 2)


if __name__ == "__main__":
    main()
