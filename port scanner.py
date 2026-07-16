import socket
import threading
from queue import Queue
from datetime import datetime

print("=" * 50)
print("          PYTHON PORT SCANNER")
print("=" * 50)

target = input("Enter IP address or domain: ").strip()

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid hostname.")
    exit()

print(f"\nScanning Target : {target}")
print(f"IP Address      : {target_ip}")
print(f"Started         : {datetime.now()}")
print("-" * 50)

queue = Queue()

open_ports = []

lock = threading.Lock()


def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            with lock:
                open_ports.append(port)
                print(f"[OPEN ] Port {port}")

        sock.close()

    except:
        pass


def worker():
    while not queue.empty():
        port = queue.get()
        scan_port(port)
        queue.task_done()


start_port = int(input("Start Port : "))
end_port = int(input("End Port   : "))

for port in range(start_port, end_port + 1):
    queue.put(port)

threads = []

for _ in range(100):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

queue.join()

print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)

if open_ports:
    print("\nOpen Ports:")
    for port in sorted(open_ports):
        print(port)
else:
    print("No open ports found.")

print("\nFinished :", datetime.now())
