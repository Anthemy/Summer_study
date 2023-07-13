import urllib.request
import urllib.parse
import json
data = {'kw': 'spider'}
url = 'https://fanyi.baidu.com/sug'
header = {'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67'}

data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url,data=data,headers=header)
response = urllib.request.urlopen(request)
code = response.read().decode('utf-8')

content = json.loads(code)
print(content)
