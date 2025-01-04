import subprocess as sp
import threading
import os


def scan1(ip):
    print("Starting Scan 1")
    sp.Popen(f"sudo nmap -Pn -p- -A -T4 -oN nmap/scan1.txt {ip}", shell=True)
    print("Scan 1 Ended...")


def scan2(ip):
    print("Starting Scan 2")
    sp.Popen(
        f"sudo nmap -Pn -p- -A --min-rate 5000 -oN nmap/scan2.txt {ip}", shell=True
    )
    print("Scan 2 Ended...")


def scan3(ip):
    print("Starting Scan 3")
    sp.Popen(
        f"sudo nmap -Pn -sU --top-ports 500 -A -T4 -oN nmap/udp-scan.txt {ip}",
        shell=True,
    )
    print("Scan 3 Ended...")


def normal_scan(ip):
    print("Starting Normal Scan")
    sp.Popen(f"sudo nmap -sSCV -oN nmap/normal_scan.txt {ip}", shell=True)
    print("Normal Scan Ended")


# Main execution
print("Starting Nmap scan")
ip = input("Enter IP address to scan: ")

# Create directory if it doesn't exist
os.makedirs("nmap", exist_ok=True)

# Create and start threads for each scan
t1 = threading.Thread(target=scan1, args=(ip,))
t2 = threading.Thread(target=scan2, args=(ip,))
t3 = threading.Thread(target=scan3, args=(ip,))
no = threading.Thread(target=normal_scan, args=(ip,))

t1.start()
t2.start()
t3.start()
no.start()

# Join threads to wait for their completion
t1.join()
t2.join()
t3.join()
no.join()

print("All scans completed.")
