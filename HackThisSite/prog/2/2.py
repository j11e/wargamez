from io import BytesIO
from PIL import Image

import requests

def morse(morseCode):
    morseCode = morseCode.replace('/', ' / ')
    morseAlphabet ={
         ".-"   : "A",
         "-..." : "B",
         "-.-." : "C",
         "-.."  : "D",
         "."    : "E",
         "..-." : "F",
         "--."  : "G",
         "...." : "H",
         ".."   : "I",
         ".---" : "J",
         "-.-"  : "K",
         ".-.." : "L",
         "--"   : "M",
         "-."   : "N",
         "---"  : "O",
         ".--." : "P",
         "--.-" : "Q",
         ".-."  : "R",
         "..."  : "S",
         "-"    : "T",
         "..-"  : "U",
         "...-" : "V",
         ".--"  : "W",
         "-..-" : "X",
         "-.--" : "Y",
         "--.." : "Z",
         "-----" : "0",
         ".----" : "1",
         "..---" : "2",
         "...--" : "3",
         "....-" : "4",
         "....." : "5",
         "-...." : "6",
         "--..." : "7",
         "---.." : "8",
         "----." : "9",
         "/" :  " "
    }

    codes = morseCode.split(" ");
    codes = list(filter(lambda x: x != "", codes))
    print(codes)

    return ''.join([morseAlphabet[code] for code in codes])


chall_url = "https://www.hackthissite.org/missions/prog/2/PNG/"
solution_url = "https://www.hackthissite.org/missions/prog/2/index.php"

def chall2():

    ## step 1: retrieve challenge, extract image, download it
    imageSource = requests.get(chall_url, headers = {"cookie": "PHPSESSID=jr6jjsqb3vlghagaka47p5n4h7", "Referer": chall_url})

    img = open('png', 'wb')
    img.write(bytearray(imageSource.content))
    img.close()

    image = Image.open(BytesIO(imageSource.content))

    ## step 2: read pixels, extract morse
    count = 0
    data = image.getdata()
    morseCode = []

    for pix in data:
        if pix == 1:
            morseCode.append(count)
            count = 0
        
        count += 1

    print(morseCode)

    morseCode = ''.join(map(chr, morseCode))

    solution = morse(morseCode)

    if solution[0] == ' ':
        solution = solution[1:]
    
    print(morseCode)
    print(">" + solution + "<")

    solution = solution.lower()

    ## step 3: submit solution
    finalOutcome = requests.post(solution_url, headers = {"cookie": "__htsCookieNotice=1; PHPSESSID=jr6jjsqb3vlghagaka47p5n4h7", "Referer": chall_url}, data = {"solution": solution}).text

    print("is wrong" in finalOutcome and "Failure" or finalOutcome)


chall2();
