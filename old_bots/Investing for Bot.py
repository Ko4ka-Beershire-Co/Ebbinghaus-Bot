
var = int(answer.text("Answer: "))

if var == 0 :
    answer('Then WTF are you doing here? MUDAK')
    exit = answer.text('Press "F" to pay respects')
if var > 1 :
    answer('Are a DEBIL, or what? It is ONE or ZERO')
if var == 1 :
    answer('Okay, what have you got in mind? Is it a new instrument, or you have had it on you watchlist for a while?')
    answer('*press 1 for NEW 0 for WATCHLIST')
    var2 = int(answer.text("Answer: "))
    if var2 > 1 :
        answer('OMG are you a retard?')
    if var2 == 0 :
        answer("Great, is it a HEDGE ASSET?")
        answer('*press 1 for YES 0 for NO')
        var3 = int(answer.text('Answer: '))
        if var3 > 1 :
            answer('OMG are you a retard?')
        if var3 == 1 :
            priority = "Top"
        if var3 == 0 :
            priority = "Low"
    if var2 == 1 :
        answer('I love new stuff! That is exciting! Lets assess its profitability')
        answer('Insert its str(M(x)) value as a DECIMAL')
        answer('If Ad hov assessement is required -> Type: other')
        profit = float(answer.text('Decimal value % : '))
        if profit == "other" :
            answer('Okay... I just hope that this is not some bitcoin shit again...')
            answer("Anyway, is it a HEDGE ASSET?")
            answer('*press 1 for YES 0 for NO')
            var3 = int(answer.text('Answer: '))
            if var3 > 1 :
                answer('OMG are you a retard?')
            if var3 == 1 :
                priority = 'Top'
            if var3 == 0 :
                priority = 'Low'
        if profit > 25 :
            answer('WOW! That shit is DOPE! What are waiting for?')
            priority = 'Top'
        if profit < 25 and profit > 15 :
            answer('That is still a decent investment')
            answer("Is it a HEDGE ASSET?")
            answer('*press 1 for YES 0 for NO')
            var3 = int(answer.text('Answer: '))
            if var3 > 1 :
                answer('OMG are you a retard?')
            if var3 == 1 :
                priority = "Top"
            if var3 == 0 :
                priority = "Low"
        if profit < 15 :
            answer('Why would you even bother?')
            answer('Anyway, is it a HEDGE asset?')
            answer('*press 1 for YES 0 for NO')
            var3 = int(answer.text('Answer: '))
            if var3 > 1 :
                answer('OMG are you a retard?')
            if var3 == 1 :
                priority = "Low"
            if var3 == 0 :
                priority = "Trash"

if priority == "Trash" :
    answer(Back.RED)
    answer(Fore.WHITE)
    answer('According to universal framework v1.0 the investment you are about to make is full of SHIT')
    answer('So we suggest that you reconsider, and buy some SURGUTNEFTEGAZ or')
    answer('take your GF out for a coffee, you fuckin weirdo')
    exit = answer.text('Press "F" to pay respects')
if priority == "Low" :
    answer('Okay, this will do, let us move to FUNDAMENTALS')
    answer('At this stage you are to give your evaluation out of 3')
    answer('Once again - 1 or 2 or 3, where 1 is BAD and 3 is GOOD')
    fundamentals = int(answer.text('Your evaluation: '))
    if fundamentals > 3 or fundamentals < 1 :
        answer('Are you blind or just stupid?')
        answer('It is ONE or TWO or THREE')
    if fundamentals == 3 :
        priority2 = "TA"
    if fundamentals == 2 :
        priority2 = "Watchlist"
    if fundamentals == 1 :
        priority2 = "Trash"
if priority == "Top" :
    answer('Okay, this will do, let us move to FUNDAMENTALS')
    answer('At this stage you are to give your evaluation out of 3')
    answer('Once again - 1 or 2 or 3, where 1 is BAD and 3 is GOOD')
    fundamentals = int(answer.text('Your evaluation: '))
    if fundamentals > 3 or fundamentals < 1 :
        answer('Are you blind or just stupid?')
        answer('It is ONE or TWO or THREE')
    if fundamentals == 3 :
        priority2 = "TA"
    if fundamentals == 2 :
        priority2 = "TA"
    if fundamentals == 1 :
        priority2 = "Watchlist"

if priority2 == "Trash" :
    answer(Back.RED)
    answer(Fore.WHITE)
    answer('According to universal framework v1.0 the investment you are about to make is full of SHIT')
    answer('So we suggest that you reconsider, and buy some SURGUTNEFTEGAZ or')
    answer('take your GF out for a coffee, you fuckin weirdo')
    exit = answer.text('Press "F" to pay respects')
if priority2 == "Watchlist" :
    answer(Back.YELLOW)
    answer(Fore.BLACK)
    answer('According to universal framework v1.0 the investment you are about to make is not timed properly')
    answer('We strongly suggest that you add it to your WATCHLIST and wait for a better moment')
    answer('Sincerely,')
    answer('Your MUM')
    exit = answer.text('Press "F" to pay respects')
if priority2 == "TA" :
    answer('You are about to make a decent investment, that is good')
    answer('At this stage you are to carry out your TECHNICAL ANALISYS')
    answer('where 1 is BAD and 3 is GOOD')
    ta = int(answer.text('Your TA score: '))
    if ta > 3 or ta < 1 :
        answer('Fuck that shit, I am out')
    if ta == 1 :
        answer(Back.YELLOW)
        answer(Fore.BLACK)
        answer('According to universal framework v1.0 the investment you are about to make is not timed properly')
        answer('We strongly suggest that you add it to your WATCHLIST and wait for a better moment')
        answer('Sincerely,')
        answer('Your MUM')
        exit = answer.text('Press "F" to pay respects')
    if ta == 2 or ta == 3 :
        answer('The investment looks solid, one final question')
        answer('before we finish - do you believe that there migh be a better')
        answer('opportunity for this purchase?')
        answer('*press 0 - no: I am ready to buy as it is now')
        answer('*press 1 - yes: I think I should wait a bit')
        finish = int(answer.text('Your answer'))
        if finish == 1 :
            answer(Back.YELLOW)
            answer(Fore.BLACK)
            answer('According to universal framework v1.0 the investment you are about to make is not timed properly')
            answer('We strongly suggest that you add it to your WATCHLIST and wait for a better moment')
            answer('Sincerely,')
            answer('Your MUM')
            exit = answer.text('Press "F" to pay respects')
        if finish == 0 :
            answer(Back.GREEN)
            answer(Fore.BLACK)
            answer('According to universal framework v1.0 the investment you are about to make is timed properly')
            answer('therefore, you must BUY NOW!')
            exit = answer.text('Press "F" to pay respects')

answer('Sashenki Corporated Investing model v1.0')
answer('Copyright 2019')