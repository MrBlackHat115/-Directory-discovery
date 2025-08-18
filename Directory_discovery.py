#!/usr/bin/env python3
import requests

target_url = input('Enter the target\'s URL (Ex. https://example.com/): ').strip()
wordlist_path = input('Enter the wordlist file path (Ex. wordlist.txt): ').strip()

# Ensure URL ends with a slash
if not target_url.endswith('/'):
    target_url += '/'

try:
    with open(wordlist_path, 'r') as wordlist_file:
        for word in wordlist_file:
            word = word.strip()  # Remove spaces/newlines
            if not word:  # Skip empty lines
                continue
            
            url = target_url + word
            try:
                response = requests.get(url, timeout=5)
                if response.status_code == 200:
                    print(f'[+] Directory found: {url} (200 OK)')
            except requests.exceptions.ConnectionError:
                print(f'[!] Could not connect to {target_url} — website may not exist.')
                break
            except requests.RequestException:
                pass
except FileNotFoundError:
    print(f'[!] Wordlist file {wordlist_path} not found.')
