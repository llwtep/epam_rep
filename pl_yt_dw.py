from pytubefix import Playlist
from pytubefix.cli import on_progress
import os



def playlist_downloader(url):
    pl=Playlist(url)
    video_title=[]
    for video in pl.videos:
        ys=video.streams.get_audio_only()
        title=video.title.replace(" ", '_')
        ys.download(output_path='yt_videos',)
        video_title.append(title)
    i = 1
    for filename in os.listdir('yt_videos'):
        if filename.endswith('.m4a'):
            new_name=f'{i}.m4a'
            os.rename(f'yt_videos/{filename}', f'yt_videos/{new_name}')
            i += 1
    return video_title




