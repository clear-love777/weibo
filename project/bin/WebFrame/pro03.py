import requests
headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'username':'root','password':'123456'}
r = requests.post('http://127.0.0.1:8080',headers=headers,params=payload)
print(r)