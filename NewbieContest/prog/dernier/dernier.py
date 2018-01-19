import requests

url = "https://www.newbiecontest.org/epreuves/prog/prog14.php"
cookies = { "PHPSESSID": "608f7d69a35dac14cb21cb195f10a167" }

def playTheGame():
    r = requests.get(url, cookies=cookies)
    print("Received: " + r.text)
    init_state = r.text.split("\n")[2]

    print("Initial state: " + init_state)

    while True:
        return

if __name__ == '__main__':
    playTheGame()
