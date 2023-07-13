import urllib.request
import urllib.parse


def creat_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&'
    data = {
        'start': (page-1)*20,
        'limit': 20
    }
    data_url = urllib.parse.urlencode(data)
    url = base_url+data_url
    header = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.67'
    }
    return urllib.request.Request(url=url, headers=header)

def get_content(request):
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')

def save(page, content):
    name = 'douban'+str(page)+'.json'
    with open(name,'w',encoding='utf-8') as file:
        file.write(content)

start = int(input("请输入开始页码: "))
end = int(input("请输入结束页码: "))
for i in range(start,end+1):
    request = creat_request(i)
    content = get_content(request)
    save(i,content)