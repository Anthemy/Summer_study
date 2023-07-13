import urllib.request
import urllib.parse

def creat_request(page):
    base_url = 'https://spa3.scrape.center/api/movie/?'
    data = {
        'limit': 10,
        'offset': (page-1)*10,
    }
    data_url = urllib.parse.urlencode(data)
    url = base_url+data_url
    print(url)
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67'
    }
    return urllib.request.Request(url=url, headers=header)

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def save(page, content):
    name = 'spa3_'+str(page)+'.json'
    with open(name,'w',encoding='utf-8') as file:
        file.write(content)

start = int(input('请输入起始页数: '))
end = int(input('请输入截止页数: '))
for page in range(start,end+1):
    request = creat_request(page)
    content = get_content(request)
    save(page,content)
