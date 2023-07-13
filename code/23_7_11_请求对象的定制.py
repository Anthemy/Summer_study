import urllib.request

url = 'https://www.baidu.com/'
headers = {'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67'}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
code = response.read().decode()
print(code)