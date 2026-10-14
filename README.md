Overview :-
Mini Nmap Network Scanner is a Python-based GUI application that scans a target IP address for open TCP ports. It identifies common network services and attempts to retrieve service banners to gather basic information about the services running on open ports.

The application uses Python's socket module for network communication, ThreadPoolExecutor for concurrent port scanning, and Tkinter for the graphical user interface.

Features :-
Port Scanning: Scans a specified range of TCP ports on a target IP address.
Service Identification: Identifies common services such as HTTP, HTTPS, SSH, FTP, DNS, and SMTP.
Banner Grabbing: Attempts to retrieve service response banners from open ports.
Multithreading: Uses ThreadPoolExecutor to scan multiple ports concurrently.
Graphical User Interface: Provides a simple interface built with Tkinter.
Scan Results: Displays open ports, their associated services, and retrieved banners.
Scrollable Output: Makes it easier to view scan results.

🛠️ Technologies Used :-
Python 3 — Core programming language.
Socket — Establishes TCP connections and checks port availability.
Concurrent Futures — Enables concurrent scanning using a thread pool.
Tkinter — Creates the graphical user interface.
ScrolledText — Displays scan results in a scrollable text area.


⚙️ How It Works :-
The user specifies a target IP address and port range.
The program attempts TCP connections to each port using Python's socket module.
A successful connection indicates that the port is accepting TCP connections.
The program maps known port numbers to common service names.
It attempts to retrieve a banner from each open port.
Results are displayed in the Tkinter interface.
A thread pool allows multiple ports to be scanned concurrently.
