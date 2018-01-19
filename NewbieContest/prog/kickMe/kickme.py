"""
WHOIS-handling code inspired from https://github.com/sopel-irc/sopel-extras/blob/master/whois.py
Which is "Copyright 2014, Ellis Percival (Flyte) sopel@failcode.co.uk
Licensed under the Eiffel Forum License 2."
So, yeah.
"""

from sopel import module
from sopel.module import event, rule
from time import sleep
import hashlib

def setup(bot):
    bot.memory["whois"] = {}

def send_whois(bot, nick):
    bot.write(["WHOIS", nick])

def get_whois(bot, nick):
    i = 0
    while nick not in bot.memory["whois"] and i < 4:
        i += 1
        sleep(1)
    
    if nick not in bot.memory["whois"] or bot.memory["whois"][nick] is None:
        print("Failed :/")

    return bot.memory["whois"][nick]

def whois(bot, nick):
    send_whois(bot, nick)
    return get_whois(bot, nick)

@rule(r".*")
@event("319")
def whois_channels_reply(bot, trigger):
    nick = trigger.args[1]
    bot.memory['whois'][nick] = trigger.args


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    
    return a


@module.rule('.*')
def kickme(bot, trigger):
    print("received " + trigger  +" (group : " + trigger.group() + ")")

    if trigger == "ok bot, casse-toi":
        bot.join("#test_lzjd3")
        bot.say("coucou", "#test_lzjd3")
        time.sleep(5)
        # kick(bot, "#test_lzjd3 lzjd ")
        bot.write(['KICK', "#test_lzjd3", "lzjd"], "casse-toi toi-même bee-atch")
        time.sleep(5)
        bot.quit("ok :(")

    if trigger == "ok bot, go kickMe":
        bot.msg('Daneel', '.challenge_kickme start')
        print("sending .challenge_kickme start")

    if 'terme de la suite de Fibonacci ?' in trigger:
        # "Quel est le hash md5 du Neme terme de la suite de Fibonacci ?"
        # extract N then calculate Nth Fibonacci number
        term = int(trigger.split(" ")[6][:-3])
        nth_fibo = fibonacci(term)

        # find out which channel Daneel joined (#KM-***) and join it
        chans = whois(bot, "Daneel")
        print("Daneel is in " + ','.join(chans))
        for chan in chans[2].split(" "):
            if "KM_" in chan:
                channel = "#" + chan.split("#")[1]
                break

        print("joining " + channel)
        bot.join(channel)

        # send challenge response
        print("Replying with " + hashlib.md5(str(nth_fibo).encode("ascii")).hexdigest())
        bot.msg('Daneel', ".challenge_kickme " + hashlib.md5(str(nth_fibo).encode("ascii")).hexdigest())

        # I don't know how to detect being opped so let's just wait ¯\_(ツ)_/¯
        sleep(1)
        bot.write(['KICK', channel, "Daneel"], "gimme dat flag")
        
