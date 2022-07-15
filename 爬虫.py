import requests
url='https://music.163.com'
a=requests.get(url)
print(a.text)
