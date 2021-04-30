# '\n' - перевод строки;


import requests
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5h://739407857:6EK4KkOP@grsst.s5.opennetwork.cc:999'}

TOKEN = '1061314536:AAGn8AxOXWaxTDa55yQS5ACmoKqYszkakk4'

bot = telebot.TeleBot(TOKEN)

currentDT = datetime.datetime.now()

Weekday = ("%a" % currentDT.isoweekday())
Hour = ("%d" % currentDT.hour)
Minute = ("%d" % currentDT.minute)
Second = ("%d" % currentDT.second)


@bot.message_handler(commands=['alarm'])
#def send_welcome(message):
# Питерская
# If loop is required -> while (count < x):
count = 0
if Weekday <= '5' and Hour == '10' and Minute == '0' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
    count = count + 1
if Weekday <= '5' and Hour == '01' and Minute == '45' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
    count = count + 1
# MOEX
if Weekday <= '5' and Hour == '09' and Minute == '30' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
    count = count + 1
if Weekday <= '5' and Hour == '18' and Minute == '0' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
    count = count + 1
# NYSE
if Weekday <= '5' and Hour == '12' and Minute == '0' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
if Weekday <= '5' and Hour == '17' and Minute == '30' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
if Weekday <= '5' and Hour == '00' and Minute == '0' and Second == '0':
    bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')

bot.polling(none_stop=True)
