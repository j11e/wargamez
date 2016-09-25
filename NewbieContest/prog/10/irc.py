# -*- coding: utf-8 -*-

from sopel import module

def rot13(txt):
    inalph = 'abcdefghijklmnopqrstuvwxyz'
    outalph = inalph[13:] + inalph[:13]
 
    inalph += inalph.upper()
    outalph += outalph.upper()

    return ''.join([ ciph[alph.index(char)] for char in txt ])


@module.commands("echo", "repeat")
def echo(bot, trigger):
    bot.reply(trigger.group)
