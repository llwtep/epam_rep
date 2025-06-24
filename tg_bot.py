import telebot
import os
from yt_dw import yt_downloader
import re

bot = telebot.TeleBot('7392391807:AAF7E1AYfhuRy69NzSYoxbtjyJm4UWHaZ0w')
incorrect_input = False



@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')


@bot.message_handler(commands=['send'])
def send(message):
    with open('yt_audios/1.m4a', 'rb') as audio:
        bot.send_audio(message.chat.id, audio, timeout=60)


@bot.message_handler()
def main2(message):
    global incorrect_input
    youtube_pattern = re.compile(r"^(https?://)?(www\.)?(youtube\.com|youtu\.be)/")
    if youtube_pattern.match(message.text):
        url = message.text
        
        bot.send_message(message.chat.id, "Загружается, пожалуйста подождите..")

        folder_path = yt_downloader(url)
        if folder_path is None or not os.path.exists(folder_path):
            bot.send_message(message.chat.id, "Ошибка при загрузке аудио. Проверь ссылку или попробуй другое видео.")
            return


        try:
            with open(folder_path, 'rb') as audio:
                bot.send_audio(message.chat.id, audio, timeout=60)
                bot.delete_message(message.chat.id, message.message_id + 1)
            if os.path.isfile(folder_path):
                os.remove(folder_path)
                print(f"Файл {folder_path} успешно удален")
            else:
                print(f"Файл {folder_path} не найден")
        except Exception as e:
            print(f"Ошибка при отправке файла {folder_path}: {e}")
            bot.send_message(message.chat.id, "Ошибка при отправке аудио. Свяжитесь с разработчиком.")

    else:
        hello_list = ["hello", "привет", "hi"]
        if any(message.text.lower() == greetings for greetings in hello_list):
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
        else:
            bot.send_message(message.chat.id, 'Ссылку с ютуба киньте пожалуйста')

            incorrect_input = True



bot.infinity_polling()
