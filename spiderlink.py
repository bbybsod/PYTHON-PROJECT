import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin

print('TikTOk    : Sean.myxzu')
print('Instagram : sean.myxzu')

def get_links(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        links = set()
        for tag in soup.find_all("a", href=True): 
            full_url = urljoin(url, tag["href"])
            links.add(full_url)
        
        return links
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return set()

def extract_params(links):
    params = set()
    for link in links:
        parsed = urlparse(link)
        if parsed.query: 
            params.add(link)
    
    return params

if __name__ == "__main__":
    target_url = input("Masukkan URL target: ") 
    found_links = get_links(target_url)
    param_links = extract_params(found_links)

    print("\n[+] Ditemukan Link:")
    for link in found_links:
        print(link)

    print("\n[+] Ditemukan Link dengan Parameter:")
    for link in param_links:
        print(link)
 
def check_link(url):
    try:
        response = requests.get(url, timeout=5)
        print(f"[+] {url} --> {response.status_code}")
    except requests.exceptions.RequestException:
        print(f"[-] {url} --> Tidak dapat diakses")

print("\n[+] Scan Status HTTP Link:")
for link in found_links:
    check_link(link)
