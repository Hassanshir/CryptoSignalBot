
from telegram import Bot
from telegram.ext import Updater, CommandHandler

TOKEN = "8495322824:AAE0t6Wq5btvE2NTY1278KXeJqqTyDWh2Ms"
CHAT_ID = "5264411685"

def start(update, context):
    update.message.reply_text("Bot is now active ✔️")

def alert(message):
    bot = Bot(TOKEN)
    bot.send_message(chat_id=CHAT_ID, text=message)

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    print("Bot is running...")

if __name__ == '__main__':
    main()
