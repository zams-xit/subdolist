import requests
import json
import sys
from colorama import Fore, Style

def print_ascii_art():
    ascii_art = r"""
   _____       __        __      __    _      __ 
  / ___/__  __/ /_  ____/ /___  / /   /_/____/ /_
  \__ \/ / / / __ \/ __  / __ \/ /   / / ___/ __/
 ___/ / /_/ / /_/ / /_/ / /_/ / /___/ /__  / /_  
/____/\__,_/_.___/\__,_/\____/_____/_/____/\__/  
                                                 
    """
    print(ascii_art)
    print(f"{Fore.YELLOW}[ INF ] This tool is currently in beta testing. We welcome your feedback to improve its functionality.")
    print()

def get_subdomains(domain):
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        subdomains = set()
        for entry in data:
            subdomain = entry['name_value']
            subdomains.add(subdomain)

        return subdomains

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[ ERR ] Error fetching data")
        return set()

def print_subdomains(subdomains, domain):
    if subdomains:
        print(f"{Fore.GREEN}Subdomains and original domains for {domain}:")
        print()
        for index, subdomain in enumerate(sorted(subdomains), start=1):
            print(f"{Fore.WHITE}[ {index} ] {subdomain}")
        print(f"{Fore.WHITE}[ {len(subdomains) + 1} ] {domain}")
        print()
        print(f"{Fore.GREEN}Thank you for using SubdoList Tools")
    else:
        print(f"{Fore.WHITE}[ ERR ] No subdomains found for {domain}.")

if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] != '-s':
        print("Use : subdolist -s domain.name")
        sys.exit(1)

    domain = sys.argv[2]
    print_ascii_art()
    subdomains = get_subdomains(domain)
    print_subdomains(subdomains, domain)