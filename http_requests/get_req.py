import requests

# Get with params
payload = {'page': 2, 'count': 25}
r = requests.get('https://httpbin.org/get', params=payload)

print(r.status_code)

# Get with basic auth
r1 = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))

print(r1.text)

# Get with timeout
r2 = requests.get('https://httpbin.org/delay/6', timeout=3)
print(r2)