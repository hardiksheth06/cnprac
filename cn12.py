import socket
import sys
import ipaddress

def is_valid_domain(domain):
    """Check if the input is a valid domain name."""
    try:
        return all(len(x) and len(x) <= 63 and x.isalnum() or x.startswith('xn--') or set(x) <= {'-', '.'} for x in domain.split('.'))
    except:
        return False

def is_valid_ip(ip):
    """Check if the input is a valid IP address."""
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def reverse_dns_lookup(ip_address):
    """Perform reverse DNS lookup."""
    try:
        domain_name = socket.gethostbyaddr(ip_address)
        return f"Domain name for IP {ip_address}: {domain_name[0]}"
    except socket.herror:
        return f"No domain name found for IP {ip_address}"

def forward_dns_lookup(domain):
    """Perform forward DNS lookup."""
    try:
        ip_address = socket.gethostbyname(domain)
        return f"IP address for domain {domain}: {ip_address}"
    except socket.gaierror:
        return f"No IP address found for domain {domain}"

def dns_lookup():
    while True:
        print("\nDNS Lookup Tool")
        print("1. Look up a domain from an IP address (Reverse DNS)")
        print("2. Look up an IP address from a domain (Forward DNS)")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ").strip()
        
        if choice == '1':
            ip_address = input("Enter the IP address: ").strip()
            if is_valid_ip(ip_address):
                print(reverse_dns_lookup(ip_address))
            else:
                print("Invalid IP address. Please try again.")
        
        elif choice == '2':
            domain = input("Enter the domain name: ").strip()
            if is_valid_domain(domain):
                print(forward_dns_lookup(domain))
            else:
                print("Invalid domain name. Please try again.")
        
        elif choice == '3':
            print("Thank you for using the DNS Lookup Tool. Goodbye!")
            sys.exit(0)
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    dns_lookup()
