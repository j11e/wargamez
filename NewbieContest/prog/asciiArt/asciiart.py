from sopel import module
from sopel.module import event, rule
from time import sleep

# dict of known letters. Format: "ascii_art" => "letter"
ascii_dict = {}

def save_ascii_dict():
    print("saving dict")
    f = open("/home/jd/asciiDict", "w")

    for k,v in ascii_dict.items():
        f.write(k+"::"+v+"\n")
    
    f.close()

def load_ascii_dict():
    print("loading dict")
    f = open("/home/jd/asciiDict", "r")

    for line in f:
        try:
            k, v = line.split("::")
            ascii_dict[k] = v.strip()
        except ValueError:
            pass
    
    f.close()


@module.rule('.*')
def asciiart(bot, trigger):
    print("received " + trigger)

    if trigger == "ok bot, go asciiArt" or trigger == "again":
        load_ascii_dict()
        bot.msg('Daneel', '.challenge_asciiart start')


    if trigger[0] == '0' and trigger[-1] == '0':
        trigger = trigger[1:-1]

        line_length = int(len(trigger) / 6)
        split_string = [trigger[line_length*i : line_length *(i+1)] for i in range(6)]

        print("Challenge is: ")
        for line in split_string:
            print(line)

        print("splitting individual letters")
        guessed_string = ""
        ascii_letters = []
        letter_start = 0
        for i in range(line_length):
            if split_string[0][i] == " " \
                    and split_string[1][i] == " " \
                    and split_string[2][i] == " " \
                    and split_string[3][i] == " " \
                    and split_string[4][i] == " " \
                    and split_string[5][i] == " ":
                ascii_letter  = split_string[0][letter_start:i] + split_string[1][letter_start:i]
                ascii_letter += split_string[2][letter_start:i] + split_string[3][letter_start:i]
                ascii_letter += split_string[4][letter_start:i] + split_string[5][letter_start:i]

                ascii_letters.append(ascii_letter)

                letter_start = i+1

                if ascii_letter in ascii_dict:
                    guessed_string += ascii_dict[ascii_letter]
                else:
                    guessed_string += "?"

        if "?" in guessed_string:
            print("Best guess: %s" % guessed_string)
            translation = input("What's it really mean? ")
            if len(translation) != 6:
                print("Translation should be 6 chars long...")
            else:
                print("Ok, taking note.")
                for i in range(6):
                    ascii_letter = ascii_letters[i]
                    char = translation[i]

                    if ascii_letter not in ascii_dict:
                        ascii_dict[ascii_letter] = char

                save_ascii_dict()
        else:
            print("I know what that means: %s. Replying to Daneel now." % guessed_string)
            bot.msg("Daneel", ".challenge_asciiart %s" % guessed_string)
