# '\n' - перевод строки;
# Alarm clock notification module

# print ("Current Year is: %d" % currentDT.year)
# print ("Current Month is: %d" % currentDT.month)
# print ("Current Day is: %d" % currentDT.day)
# print ("Current Hour is: %d" % currentDT.hour)
# print ("Current Minute is: %d" % currentDT.minute)
# print ("Current Second is: %d" % currentDT.second)
# print ("Current Microsecond is: %d" % currentDT.microsecond)
# bot.send_message(message.chat.id, 'Я РАБОТАЮЮЮЮЮЮ!!!!! ДААА СУКА')
# send the previous command at the end of a sequence))))


# import requests
import telebot
from telebot import apihelper, TeleBot
import time

apihelper.proxy = {'https': 'socks5://739407857:6EK4KkOP@grsst.s5.opennetwork.cc:999'}

TOKEN = '1061314536:AAGn8AxOXWaxTDa55yQS5ACmoKqYszkakk4'

bot: TeleBot = telebot.TeleBot(TOKEN)


# Alarm module v 1.12
@bot.message_handler(commands=['alarm'])
def send_notification(message):
    alarm = True
    count = 0  # parenthesis?
    bot.send_message(message.chat.id, 'This command is valid for 24 hours \n'
                                      'so you will have to turn it on every morning...\n'
                                      'Someday we will fix that)\n'
                                      'P.S: This command notifies you about market sessions\n'
                                      'pre-market and other crap) Cheers!!!')
    while count < 7:
        import datetime

        currentDT = datetime.datetime.now()

        Date = ('%a' % currentDT.date())
        Weekday = ("%a" % currentDT.isoweekday())
        Hour = ("%d" % currentDT.hour)
        Minute = ("%d" % currentDT.minute)
        Second = ("%d" % currentDT.second)
        # Dates
        if Date == 'datetime.date(2020, 1, 31)' and Hour == '12' and Minute == '0' and Second == '0':
            bot.send_message(message.chat.id, 'Skynet wishes happy birthday to Andey Fedorov!!!\n'
                                              'Love, peace and STONKS be with you!!!')
            count = 1
            count = count + 1
            if count == 6:
                time.sleep(5)
        # SPBEX
        if Weekday <= '5' and Hour == '10' and Minute == '0' and Second == '0':
            bot.send_message(message.chat.id, 'SPBEX: market session is starting')
            count = 1
            if count == 1:
                time.sleep(5)
        if Weekday <= '5' and Hour == '1' and Minute == '45' and Second == '0':
            bot.send_message(message.chat.id, 'SPBEX: market session has ended')
            bot.send_message(message.chat.id, 'Alarm is off, please restart the command\n'
                                              'if required. P.S. why are you still awake?')
            count = 7
            if count == 7:
                time.sleep(5)
        # Easter egg
        if Weekday <= '7' and Hour == '15' and Minute == '20' and Second == '0':
            bot.send_message(message.chat.id, 'A friendly reminder: Lesha is gay))))')
            count = 1.5
            if count == 1.5:
                time.sleep(5)
        # MOEX
        if Weekday <= '5' and Hour == '10' and Minute == '0' and Second == '0':
            bot.send_message(message.chat.id, 'MOEX: market session is starting')
            count = 3
            if count == 3:
                time.sleep(5)
        if Weekday <= '5' and Hour == '18' and Minute == '45' and Second == '0':
            bot.send_message(message.chat.id, 'MOEX: market session has ended')
            count = 4
            if count == 4:
                time.sleep(5)
        # NYSE
        if Weekday <= '5' and Hour == '12' and Minute == '0' and Second == '0':
            bot.send_message(message.chat.id, 'NYSE: pre-market session is starting')
            count = 5
            if count == 5:
                time.sleep(5)
        if Weekday <= '5' and Hour == '17' and Minute == '30' and Second == '0':
            bot.send_message(message.chat.id, 'NYSE: market session is starting')
            count = 2
            if count == 2:
                time.sleep(5)
        if Weekday <= '5' and Hour == '0' and Minute == '0' and Second == '0':
            bot.send_message(message.chat.id, 'NYSE: market session has ended')
            count = 7
            alarm = False
            if count == 7:
                time.sleep(5)


# Sessions v 1.0 using Boole
@bot.message_handler(commands=['sessions'])
def send_snapshot(message):
    import datetime
    currentDT = datetime.datetime.now()

    Date = ('%a' % currentDT.date())
    Weekday = ("%a" % currentDT.isoweekday())
    Hour = ("%d" % currentDT.hour)
    Minute = ("%d" % currentDT.minute)
    Second = ("%d" % currentDT.second)

    SPBEX = False
    MOEX = False
    NYSEp = False
    NYSE = False
    Lesha = False

    # SPBEX
    if Weekday <= '5' and '10' <= Hour <= '2':
        SPBEX = True
    # Easter egg
    if Weekday <= '7':
        Lesha = True
    # MOEX
    if Weekday <= '5' and '10' <= Hour <= '19':
        MOEX = True
    # NYSEp
    if Weekday <= '5' and '12' <= Hour < '17':
        NYSEp = True
    if Weekday <= '5' and Hour == '17' and Minute < '30':
        NYSEp = True
    #NYSE
    if Weekday <= '5' and Hour == '17' and Minute >= '30':
        NYSE = True
    if Weekday <= '5' and '18' <= Hour <= '0':
        NYSE = True

    if SPBEX:
        bot.send_message(message.chat.id, 'SPBEX: ongoing market session')
    if not SPBEX:
        bot.send_message(message.chat.id, 'SPBEX: market is closed')

    if MOEX:
        bot.send_message(message.chat.id, 'MOEX: ongoing market session')
    if not MOEX:
        bot.send_message(message.chat.id, 'MOEX: market is closed')

    if NYSEp:
        bot.send_message(message.chat.id, 'NYSE: ongoing pre-market session')
    if NYSE:
        bot.send_message(message.chat.id, 'NYSE: ongoing market session')
    if not NYSE and not NYSEp:
        bot.send_message(message.chat.id, 'NYSE: market is closed')

    if Lesha:
        bot.send_message(message.chat.id, 'Lesha: still gay')


bot.polling(none_stop=True)
