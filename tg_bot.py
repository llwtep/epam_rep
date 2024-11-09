import telebot
import os
from yt_dw import yt_downloader, get_name
from pl_yt_dw import playlist_downloader
import re
bot = telebot.TeleBot('7392391807:AAF7E1AYfhuRy69NzSYoxbtjyJm4UWHaZ0w')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
@bot.message_handler(commands=['send'])
def send(message):
    with open('yt_audios/1.m4a', 'rb') as audio:
        bot.send_audio(message.chat.id, audio, timeout=60)

@bot.message_handler()
def main2(message):
    youtube_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/")
    youtube_pattern_playlist = re.compile(r"^(https?://)?(www\.)?youtube\.com/playlist\?list=[\w-]+$")
    if youtube_pattern_playlist.match(message.text):##if the url correct
        url=message.text
        bot.send_message(message.chat.id, "Загружается, пожалуйста подождите..")
        video_title=playlist_downloader(url)
        try:
            j=1
            for i,filename in enumerate(os.listdir('yt_videos')):
                with open(f'yt_videos/{j}.m4a', 'rb') as audio:
                    title=video_title[i]
                    bot.send_audio(message.chat.id, audio,title=title, timeout=60)
                    j+=1
            i=1
            for filename in os.listdir('yt_videos'):
                os.remove(f'yt_videos/{i}.m4a')
                i+=1
            bot.delete_message(message.chat.id, message.message_id+1)

        except Exception as e:
            print(f'Error as {e}')



    elif youtube_pattern.match(message.text):
        url = message.text
        bot.send_message(message.chat.id, "Загружается, пожалуйста подождите..")
        yt_downloader(url)
        folder_path = 'yt_audios/1.m4a'
        try:
            with open(folder_path, 'rb') as audio:
                bot.send_audio(message.chat.id, audio, title=get_name(url), timeout=60)
                bot.delete_message(message.chat.id, message.message_id+1)
            if os.path.isfile(folder_path):
                os.remove(folder_path)
                print(f"Файл {folder_path} успешно удален")
            else:
                print(f"Файл {folder_path} не найден")
        except Exception as e:
            print(f"Ошибка при отправке файла {folder_path}: {e}")

    else:##if message is not correct
        hello_list=["hello", "привет", "hi"]
        if any(message.text.lower() == greetings for greetings in hello_list):
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
        else:
            bot.send_message(message.chat.id, 'Ошибка, предоставь видео с ютуба')




bot.infinity_polling()