#DNSmap - Subdomain & Reverse DNS Resolver

Author: m4lw4r2  

DNSmap is a fast multithreaded Python tool for subdomain enumeration with optional reverse DNS (PTR) lookup support.  
Ideal for use onME.md faylı (Android) or Pydroid platforms.

---

## Features

- Subdomain resolution with A record lookup
- Optional reverse DNS (PTR) record lookup
- Wordlist customizable (TXT format)

---

## Installation

### 1. Clone the repository

git clone https://github.com/m4lw4r2/dnsmap.git
cd dnsmap

2. Install required modules

For Termux or Pydroid:

pip install dnspython 
pip install pyfiglet

If you see error ModuleNotFoundError: No module named 'dns', install dnspython as shown above.

⸻

Usage

Run the tool

python dnsmap.py

Then follow the prompts:
 • Target domain – example: example.com
 • Thread count – number of threads (e.g., 10) or press Enter for automatic detection
 • Enable reverse DNS – type yes or no

⸻

Wordlist

By default, the tool uses:

/storage/emulated/0/Download/wordlist.txt

You can edit this file or replace it with your own wordlist.

Each line in the file should contain one subdomain prefix.
Example:

www
mail
ftp
blog


⸻

Output

Results are saved to:

/storage/emulated/0/Download/results.txt

Output format:

subdomain.example.com -> 192.168.1.1 | PTR: some.reverse.host


⸻

Customize

Feel free to:
 • Change the output location
 • Modify the logic for your needs
 • Use your own wordlist

⸻

License

This project is open-source. You are free to use, modify, and share it.

⸻