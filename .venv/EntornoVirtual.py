import requests

#r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
r = requests.get('https://jsonplaceholder.typicode.com/posts/3', auth=('user', 'pass'))
r.status_code
print(r.text)
print(r.json())