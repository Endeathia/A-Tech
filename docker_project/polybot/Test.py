# import os

# import telebot

# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# bot = telebot.TeleBot(BOT_TOKEN)
# print(f"Bot Token: {BOT_TOKEN}")

# @bot.message_handler(commands=['start', 'hello'])
# def send_welcome(message):
#     bot.reply_to(message, "Howdy, how are you doing?")

# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, message.text)


# @bot.message_handler(content_types=['photo'])
# def download_image(message):
#         fileID = message.photo[-1].file_id
#         file_info = bot.get_file(fileID)
#         downloaded_file = bot.download_file(file_info.file_path)
#         with open("image.jpg", 'wb') as new_file:
#                 new_file.write(downloaded_file)
#                 bot.reply_to(message, "Image Downloaded type: " + fileID)



# bot.infinity_polling()


l = {
    "person":2,
    "tree":3,
    "jjeny":4
}

for i,b in l.items():
    print(i,b)