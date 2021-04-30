# Alarm clock notification module


# print ("Current Year is: %d" % currentDT.year)
# print ("Current Month is: %d" % currentDT.month)
# print ("Current Day is: %d" % currentDT.day)
# print ("Current Hour is: %d" % currentDT.hour)
# print ("Current Minute is: %d" % currentDT.minute)
# print ("Current Second is: %d" % currentDT.second)
# print ("Current Microsecond is: %d" % currentDT.microsecond)



# Питерская
count = 0
while count < 7:
    import datetime
    import time

    currentDT = datetime.datetime.now()

    Date = ('%a' % currentDT.date())
    Weekday = ("%a" % currentDT.isoweekday())
    Hour = ("%d" % currentDT.hour)
    Minute = ("%d" % currentDT.minute)
    Second = ("%d" % currentDT.second)
    count = 0
    print(Hour)
    if Weekday <= '5' and Hour == '17' and Minute == '7' and Second == '0':
        print('SPBEX: market session is starting')
        count = 1
        if count == 1:
            time.sleep(5)
    if Weekday <= '5' and Hour == '17' and Minute == '8' and Second == '0':
        print('SPBEX: market session has ended')
        count = 2
        if count == 2:
            time.sleep(5)
    # MOEX
    if Weekday <= '5' and Hour == '09' and Minute == '30' and Second == '0':
        print('MOEX: market session is starting')
        count = 3
    if Weekday <= '5' and Hour == '18' and Minute == '0' and Second == '0':
        print('MOEX: market session has ended')
        count = 4
    # NYSE
    if Weekday <= '5' and Hour == '12' and Minute == '0' and Second == '0':
        print('NYSE: pre-market session is starting')
        count = 5
    if Weekday <= '5' and Hour == '17' and Minute == '30' and Second == '0':
        print('NYSE: main market session is starting')
        count = 6
    if Weekday <= '5' and Hour == '00' and Minute == '0' and Second == '0':
        print('NYSE: market session has ended')
        count = 7
print('Hour')