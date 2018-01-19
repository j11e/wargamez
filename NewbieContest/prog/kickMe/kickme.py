import sopel.module
import time

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a


@sopel.module.rule('.*')
def kickme(bot, trigger):
    print("received " + trigger)

    if trigger == "ok bot, casse-toi":
        bot.join("testlzjd2")
        bot.say("coucou", "#testlzjd2")

        bot.quit("ok :(")

    if trigger == "test":
        bot.join("testlzjd2")
        bot.say("coucou", "#testlzjd2")

    if trigger == "ok bot, go kickMe":
        bot.msg('Daneel', '.challenge_kickme start')
        print("sending .challenge_kickme start")

    if 'terme de la suite de Fibonacci ?' in trigger:
        # "Quel est le hash md5 du Neme terme de la suite de Fibonacci ?"
        # extract N
        number = trigger.split(" ")[6][:-3]
        # calculate Nth Fibonacci number
        nth_fibo = fibonacci(number)
        # find out which channel Daneel joined (#KM-***)
        # "whois" sopel module?
        channel = "KM-****"
        # join #KM-***
        bot.join(channel)
        # send challenge response
        bot.msg('Daneel', ".challenge_kickme " + str(nth_fibo))
        # I don't know if I can detect being opped so let's just wait ¯\_(ツ)_/¯
        time.sleep(1)
        bot.kick("Daneel", channel)
        time.sleep(5)
        bot.quit("My work here is done.")
