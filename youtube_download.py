urls = []
print('### YouTube Download Program ###')
while True:
    url = input('URL : ')
    if url == '': break
    urls.append(url)
from pytube import YouTube
while len(urls):
    durl = urls.pop(0)
    print('Download', durl)
    try:
        yt = YouTube(durl)
        # yt.streams.filter(mime_type='video/mp4').all()
        yt.streams.get_by_itag(22).download()
    except:
        print('URL error')
print('Done')