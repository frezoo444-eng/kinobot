import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL_ID = "@kinokoduz_bot_hd"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Salom! Kino yoki multfilm kodi (raqami)ni yuboring:")

@bot.message_handler(func=lambda message: True)
def send_movie(message):
    code = message.text.strip()
    
    if code.isdigit():
        msg_id = int(code)
        try:
            bot.copy_message(
                chat_id=message.chat.id,
                from_chat_id=CHANNEL_ID,
                message_id=msg_id
            )
        except Exception:
            bot.reply_to(message, "Bunday kodli kino topilmadi.")
    else:
        bot.reply_to(message, "Iltimos, faqat raqam yuboring.")

if __name__ == '__main__':
    bot.polling(none_stop=True)
