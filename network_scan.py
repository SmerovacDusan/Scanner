import subprocess
import socket
import logging
logger = logging.getLogger(__name__)

def ping(ip: str) -> bool:
    try:
        # -n 1 = 1 ping, -w 300 = timeout 300 ms (Windows)
        result = subprocess.run(
            ["ping", "-n", "1", "-w", "300", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False


def resolve_hostname(ip: str) -> str | None:
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except Exception:
        return None


def scan_network(base_ip: str, start: int, end: int):
    active_hosts = []

    for i in range(start, end + 1):
        ip = f"{base_ip}.{i}"
        print(f"Pingování číslo {i} z {end}")
        if ping(ip):
            hostname = resolve_hostname(ip)
            active_hosts.append((ip, hostname))

    return active_hosts

def run_network_scan(zaklad_ip:str, start:str,konec:str):
    st = int(start)
    ko = int(konec)
    zak = zaklad_ip.rstrip(".")
    logger.info(f"Skenovani IP adres {zaklad_ip}.{start} - {zaklad_ip}.{konec}")
    if st == None or ko == None or zak == None:
        logger.error("Spatne zadane udaje pro sken")
        return None
    else:
        hosts = scan_network(zak, st, ko)
        logger.info("Aktivni hoste: ")
        for host in hosts:
            ip, hostname = host
            logger.info(f"IP adresa: {ip}, hostname: {hostname if not None else "Neznamy"}")
    logger.info("Konec network scanu")
    return hosts

