import sopel.module

def rotN(txt, offset=3):
    inalph =  'defghijklmnopqrstuvwxyzabc'
    outalph = 'abcdefghijklmnopqrstuvwxyz'

    inalph += inalph.upper()
    outalph += outalph.upper()

    txt = ''.join([truc for truc in txt if truc in inalph])
    
    return ''.join([ outalph[inalph.index(char)] for char in txt ])



 @sopel.module.rule('.*')
 def caesar(bot, trigger):
     print("received " + trigger)

     if trigger == ".gobot" or 'avez mal' in trigger or 'Aucun chall' in trigger:
         bot.msg('Daneel', '.challenge_caesar start')
         print("sending .challenge_caesar start")
     else:
         resp = rotN(trigger)
         resp = '.challenge_caesar {0}\n'.format(resp)

         print("sending " + resp)
       
         bot.msg('Daneel', resp)

