!pip install python-telegram-bot
!pip install adafruit-io
from telegram.ext import Updater, CommandHandler
import requests
from Adafruit_IO import Client,Feed,Data
import os
ADAFRUIT_IO_USERNAME = os.getenv('Shivam_27')
ADAFRUIT_IO_KEY = os.getenv('aio_doxv60ChS13qkYRR3MaRxXqqFOkI')
aio = Client('Shivam_27','aio_doxv60ChS13qkYRR3MaRxXqqFOkI')
TELEGRAM_TOKEN = os.getenv('1381150899:AAE1I2KYkJWiBD6y-ZBFTx_Dgn1QBNQbmkI')
def get_url():
  contents = request.get()
  url= contents['url']
  return url
def lighton(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned ON")
  bot.send_photo(chat_id, photo='https://www.securityroundtable.org/wp-content/uploads/2019/03/AdobeStock_261504199-scaled.jpeg')
def lightoff(bot, update):
  chat_id = update.message.chat_id
  bot.send_message(chat_id, text="Light has been turned OFF")
  bot.send_photo(chat_id, photo='https://ak.picdn.net/shutterstock/videos/1027638404/thumb/1.jpg?ip=x480')
u = Updater('1381150899:AAE1I2KYkJWiBD6y-ZBFTx_Dgn1QBNQbmkI')
dp = u.dispatcher
dp.add_handler(CommandHandler('lighton',lighton))
dp.add_handler(CommandHandler('lightoff',lightoff))
u.start_polling()
u.idle()
