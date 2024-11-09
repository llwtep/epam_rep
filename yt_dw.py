from pytubefix import YouTube
from pytubefix.cli import on_progress
import re
import os

def yt_downloader(url):
    yt = YouTube(url, on_progress_callback=on_progress)
    output_path = r'C:\Users\HOME\PycharmProjects\TelegramBotpythonProject\yt_audios'
    ys = yt.streams.get_audio_only()
    ys.download(output_path=output_path)
    for filename in os.listdir(output_path):
        if filename.endswith('.m4a'):
            new_path_file='1.m4a'
            os.rename(f'{output_path}/{filename}',f'{output_path}/{new_path_file}')







def get_name(url):
    title=YouTube(url).title
    title = re.sub(r'[\\/*?:"<>|]', "_", title)
    return title
















