import socket
from concurrent.futures import ThreadPoolExecutor
import tkinter as tk
from tkinter import scrolledtext

# Common port → service mapping
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP"
}

# Banner grabbing
def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ip, port))

        sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
        banner = sock.recv(1024).decode(errors="ignore").strip()

        sock.close()
        return banner[:100]
    except:
        return "No banner"

# Scan ports
def scan_ports():
    target = target_entry.get()

    try:
        start_port = int(start_port_entry.get())
        end_port = int(end_port_entry.get())
    except ValueError:
        result_box.insert(tk.END, "Invalid port numbers\n")
        return

    result_box.delete(1.0, tk.END)
    result_box.insert(tk.END, f"Scanning {target}...\n\n")

    def update_result(text):
        result_box.insert(tk.END, text)

    def scan(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            result = sock.connect_ex((target, port))

            if result == 0:
                service = COMMON_PORTS.get(port, "Unknown")
                banner = grab_banner(target, port)

                output = f"Port {port} OPEN | Service: {service}\nBanner: {banner}\n\n"
                window.after(0, update_result, output)

        finally:
            sock.close()

    # Thread pool (controlled threads)
    with ThreadPoolExecutor(max_workers=100) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan, port)


# GUI
window = tk.Tk()
window.title("Mini Nmap Scanner")
window.geometry("600x550")

tk.Label(window, text="Target IP").pack()
target_entry = tk.Entry(window, width=40)
target_entry.pack()

tk.Label(window, text="Start Port").pack()
start_port_entry = tk.Entry(window, width=40)
start_port_entry.pack()

tk.Label(window, text="End Port").pack()
end_port_entry = tk.Entry(window, width=40)
end_port_entry.pack()

scan_button = tk.Button(window, text="Scan", command=scan_ports)
scan_button.pack(pady=10)

result_box = scrolledtext.ScrolledText(window, width=70, height=25)
result_box.pack()

window.mainloop()