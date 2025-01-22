import yt_dlp



def yt_downloader(url: str):
    opts = {
        'outtmpl': "yt_audios/%(title)s.%(ext)s",
        'format': 'bestaudio[ext=m4a]',
    }
    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            filename = ydl.prepare_filename(info_dict)
            ydl.download([url])
            return filename
    except Exception as e:
        print(str(e))





