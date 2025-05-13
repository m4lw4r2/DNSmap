import dns.resolver
import dns.reversename
import concurrent.futures
import os
import multiprocessing
from pyfiglet import Figlet

# Banner display
def banner():
    f = Figlet(font='slant')
    banner_text = f.renderText("DNSmap")
    print("\033[1;32m" + banner_text + "\033[0m")
    print("\033[1;37m" + "="*50 + "\033[0m")
    print("\033[1;37mAuthor: \033[1;36mm4lw4r2\033[0m")
    print("\033[1;37mTool:   \033[1;32mSubdomain & Reverse Resolver\033[0m")
    print("\033[1;37mGitHub: \033[1;36mgithub.com/m4lw4r2\033[0m")
    print("\033[1;37m" + "="*50 + "\033[0m\n")

# DNS Resolver Configuration
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8', '1.1.1.1']
resolver.timeout = 2
resolver.lifetime = 2

# Subdomain Checker
def check_subdomain(subdomain, do_reverse):
    try:
        answers = resolver.resolve(subdomain, 'A')
        ip = answers[0].to_text()
        if do_reverse:
            try:
                rev_name = dns.reversename.from_address(ip)
                ptr = resolver.resolve(rev_name, 'PTR')[0].to_text()
            except:
                ptr = "PTR not found"
            result = f"{subdomain} -> {ip} | PTR: {ptr}"
        else:
            result = f"{subdomain} -> {ip}"
        print("[+] " + result)
        return result
    except:
        return None

# Smart thread count
def get_optimal_threads():
    cpu_count = multiprocessing.cpu_count()
    return cpu_count * 5  # For example, 4 CPU cores * 5 = 20 threads

# Main function
def main():
    banner()
    domain = input("Enter target domain (e.g. example.com): ").strip()
    wordlist_path = "/storage/emulated/0/Download/wordlist.txt"
    output_file = "/storage/emulated/0/Download/results.txt"

    if not os.path.exists(wordlist_path):
        print(f"[!] Wordlist not found: {wordlist_path}")
        return

    # Thread input AFTER domain
    try:
        user_input = input("Thread count (e.g. 10, press Enter for auto): ").strip()
        if user_input == "":
            threads = get_optimal_threads()
            print(f"[*] Auto-selected optimal thread count: {threads}")
        else:
            threads = int(user_input)
            if threads > 100:
                print("[!] Warning: More than 100 threads may freeze device or get DNS blocked.")
    except:
        threads = get_optimal_threads()
        print(f"[*] Invalid input. Auto-selected thread count: {threads}")

    reverse_input = input("Enable reverse DNS lookup? (yes/no): ").strip().lower()
    do_reverse = True if reverse_input == "yes" else False

    with open(wordlist_path, "r") as f:
        words = f.read().splitlines()

    subdomains = [f"{word.strip()}.{domain}" for word in words if word.strip()]

    print(f"\n[✓] {len(subdomains)} subdomains will be checked...\n")

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        futures = [executor.submit(check_subdomain, sub, do_reverse) for sub in subdomains]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    with open(output_file, "w") as f:
        for line in results:
            f.write(line + "\n")

    print(f"\n[✓] Done! Results saved to: {output_file}")
    banner()

if __name__ == "__main__":
    main()