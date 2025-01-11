import subprocess
import threading
import os

# Constants
NMAP_COMMANDS = {
    "scan1": {
        "cmd": "sudo nmap -Pn -p- -A -T4 -oN nmap/scan1.txt {}",
        "options": {"shell": True},
    },
    "scan2": {
        "cmd": "sudo nmap -Pn -p- -A --min-rate 5000 -oN nmap/scan2.txt {}",
        "options": {"shell": True},
    },
    "scan3": {
        "cmd": "sudo nmap -Pn -sU --top-ports 500 -A -T4 -oN nmap/udp-scan.txt {}",
        "options": {"shell": True},
    },
    "normal_scan": {
        "cmd": "sudo nmap -sSCV -oN nmap/normal_scan.txt {}",
        "options": {"shell": True},
    },
}


def scan(ip, func):
    print(f"Starting {func}")
    process = subprocess.Popen(func["cmd"].format(ip), **func["options"])
    process.wait()
    print(f"{func} Ended")


def main():
    ip = input("Enter IP address to scan: ")

    # Create directory if it doesn't exist
    os.makedirs("nmap", exist_ok=True)

    # Create and start threads for each scan
    threads = [
        threading.Thread(target=scan, args=(ip, NMAP_COMMANDS["scan1"])),
        threading.Thread(target=scan, args=(ip, NMAP_COMMANDS["scan2"])),
        threading.Thread(target=scan, args=(ip, NMAP_COMMANDS["scan3"])),
        threading.Thread(target=scan, args=(ip, NMAP_COMMANDS["normal_scan"])),
    ]

    # Start threads
    for thread in threads:
        thread.start()

    # Join threads to wait for their completion
    for thread in threads:
        thread.join()

    print("All scans completed.")


if __name__ == "__main__":
    main()
