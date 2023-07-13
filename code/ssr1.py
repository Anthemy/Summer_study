import  urllib.request


url_page_code = 'https://ssr1.scrape.center/'
urllib.request.urlretrieve(url_page_code,'ssr1.html')
response = urllib.request.urlopen(url_page_code)
print(response.getcode())