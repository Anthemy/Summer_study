import urllib.request

#定义一个url，就是我要访问的网页地址
url = 'https://ssr1.scrape.center/'

#模拟浏览器，向发送网页服务器发送浏览请求
response = urllib.request.urlopen(url)

#读取网页源码，注意解码
code = response.read().decode('UTF-8')
# code = response.read(5)   #读五个字节
# code = response.readline() #读一行
# code = response.readlines() #读取多行


print(code)

# response是HTTPResponse类型
print(type(response))

#状态码，如果是200说明正常，不正常：404，500等等
print(response.getcode())

#返回url地址
print(response.geturl())

#返回状态
print(response.getheaders())


