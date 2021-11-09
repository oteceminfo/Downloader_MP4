import pytube

url = input('url do video: ')
yt = pytube.Youtube(url)
video = yt.streams.first()
video.download()
print('Video baixado com sucesso!')
