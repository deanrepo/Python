import requests

# from requests.exceptions import HTTPError

# for url in ["https://api.github.com", "https://invalid.com"]:
#     try:
#         response = requests.get(url)

#     except HTTPError as err:
#         print(err)
    
#     else:
#         print('success')

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'}
)

print(response.content)

