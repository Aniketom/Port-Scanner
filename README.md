# 🔍 Python Port Scanner

A beginner-friendly TCP Port Scanner built using Python.

This project scans a target host for open TCP ports using Python's built-in `socket` library and multithreading to improve scanning speed.

> ⚠️ This tool is intended **only for educational purposes** and should be used **only on systems you own or have explicit permission to test**.

---

## Features

- Scan any valid IP address or hostname
- User-defined port range
- Multithreaded scanning
- Displays open ports
- Resolves hostnames to IP addresses
- Fast and lightweight
- Uses only Python standard libraries

---

## Technologies Used

- Python 3
- socket
- threading
- queue
- datetime

---

## Concepts Learned

- TCP networking
- Socket programming
- DNS resolution
- Multithreading
- Queues
- Exception handling
- Python standard library

---

## How to Run

```bash
python port_scanner.py
```

Example:

```
Enter IP address or domain: scanme.nmap.org
Start Port : 1
End Port   : 1000
```

---

## Future Improvements

- Service detection
- Banner grabbing
- UDP scanning
- Save results to a file
- Custom timeout values
- Progress bar
- GUI using Tkinter

---

## Disclaimer

This software is provided for educational purposes only. Always obtain authorization before scanning any network or system. The author is not responsible for misuse.

---

## Author

Aniket Kumar
