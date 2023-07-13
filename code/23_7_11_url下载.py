import  urllib.request


# 下载网页源代码
url_page_code = 'https://www.baidu.com/'
urllib.request.urlretrieve(url_page_code,'baidu.html')
response = urllib.request.urlopen(url_page_code)
print(response.getcode())

#下载图片
# url_image = 'https://pic4.zhimg.com/v2-149e9f641ee3d2750d4565d4c8248b2c_r.jpg?source=1940ef5c'
# urllib.request.urlretrieve(url_image,'image.jpg')
# response = urllib.request.urlopen(url_image)
# print(response.getcode())

#下载视频
# url_video = 'https://www.douyin.com/aweme/v1/play/?video_id=v0d00fg10000cibqu9rc77udok3fkfs0&line=0&file_id=7cb6446927214f39981564d29bc897d4&sign=2e03e3b1ec9bcc9da33b604e502c94f7&is_play_url=1&source=PackSourceEnum_AWEME_DETAIL&aid=6383'
# urllib.request.urlretrieve(url_video,'video.mp4')
# response = urllib.request.urlopen(url_video)
# print(response.getcode())