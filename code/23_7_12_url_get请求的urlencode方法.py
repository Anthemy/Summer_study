import urllib.parse
import urllib.request

data = {
    'wd': '周杰伦',
    'location': '中国台湾省'
}
data_url = urllib.parse.urlencode(data)
base_url = 'https://www.baidu.com/s?'
url = base_url + data_url
header = {'User-Agent':
'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67'}
request = urllib.request.Request(url=url,headers=header)
response = urllib.request.urlopen(request)
code = response.read().decode('utf-8')
print(code)