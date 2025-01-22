import telebot
import os
from yt_dw import yt_downloader
import re

bot = telebot.TeleBot('7392391807:AAF7E1AYfhuRy69NzSYoxbtjyJm4UWHaZ0w')
incorrect_input = False


# nigger
# CAACAgIAAxkBAAIDYGeRKgQgTJJEv7dedKHlW8Tx9QY-AAIiEwAChYUQSJPY5p3ou07XNgQ
# dima bilan
# CAACAgIAAxkBAAIDYWeRKiXuUAwDp2zEr_1Ug9m8A6spAAJyXQACo8UgSEGybLPw-uN1NgQ
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
        if (incorrect_input):
            incorrect_input = False
            dima_bilan_stiker = 'CAACAgIAAxkBAAIDYWeRKiXuUAwDp2zEr_1Ug9m8A6spAAJyXQACo8UgSEGybLPw-uN1NgQ'
            bot.send_message(message.chat.id, f'Наконец то поумнел иксдэ)))')
            bot.send_sticker(message.chat.id, dima_bilan_stiker)
        else:
            bot.send_message(message.chat.id, "Загружается, пожалуйста подождите..")

        folder_path = yt_downloader(url)
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
            bot.send_message(f"Ошибка при отправке аудио свяжитесь с разработчиком чтобы решить проблему")

    else:
        hello_list = ["hello", "привет", "hi"]
        if any(message.text.lower() == greetings for greetings in hello_list):
            bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!')
        elif (incorrect_input):
            stiker_id = 'CAACAgIAAxkBAAIDYGeRKgQgTJJEv7dedKHlW8Tx9QY-AAIiEwAChYUQSJPY5p3ou07XNgQ'
            bot.send_message(message.chat.id, 'Eбать ты додик бля')
            bot.send_sticker(message.chat.id, stiker_id)
        else:
            bot.send_message(message.chat.id, 'Я сказал ссылку с ютуба, не позорься:)')

            incorrect_input = True


@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    stiker_file_id = message.sticker.file_id
    print('Sticker ID:', stiker_file_id)


bot.infinity_polling()
