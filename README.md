This tool is designed to discover accessible directories on a target website using a user-provided wordlist. It works by combining each word in the list with the target URL and sending HTTP requests to check if the directory exists.

Key Features:

Scans a target website using a wordlist of potential directories.

Reports only directories that return a 200 OK status code.

Handles connection errors gracefully, stopping the scan if the website is unreachable.

Skips empty lines and continues scanning even if some requests fail.

Useful for penetration testing, security assessments, and bug bounty programs to identify publicly accessible paths.
