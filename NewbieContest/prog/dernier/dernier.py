"""
this challenge is a game of Nim. See https://en.wikipedia.org/wiki/Nim#Mathematical_theory
"""

import requests

url = "https://www.newbiecontest.org/epreuves/prog/prog14.php"
cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}

def parse_state(state):
    return list(map(int, state.split('/')))

def calc_nim_sum(state):
    nim_sum = 0
    for heap_val in state:
        nim_sum ^= heap_val

    return nim_sum

def compute_target_heap_and_value(state, nim_sum):
    for i, heap in enumerate(state):
        if heap ^ nim_sum < heap:
            return (i, heap - (heap ^ nim_sum))

def play_the_game():
    r = requests.get(url, cookies=cookies)
    print("Received: " + r.text)

    state = parse_state(r.text.split("<br><br>")[1])

    while True:
        nim_sum = calc_nim_sum(state)

        heaps_larger_than_1 = 0
        heaps_larger_than_0 = 0
        for heap in state:
            if heap > 0:
                heaps_larger_than_0 += 1

                if heap >= 2:
                    heaps_larger_than_1 += 1

        if heaps_larger_than_1 <= 1:
            print("nearing endgame")
            # nevermind if the game is already lost, this simplifies the code
            max_heap = max(state)
            target_heap = state.index(max_heap)
            target_value = max_heap - (heaps_larger_than_0 % 2)
        else:
            target_heap, target_value = compute_target_heap_and_value(state, nim_sum)
            
        target_heap += 1 # the game counts from one...
        print("Let's take " + str(target_value) + " from heap number "+ str(target_heap))
        r = requests.get(url+"?numtas="+str(target_heap)+"&nbpions="+str(target_value), cookies=cookies)
        print("Received: " + r.text)

        try:
            state = r.text.split('tat du jeu : ')[2].split('<br')[0]
            state = parse_state(state)
        except Exception:
            return

        print("new state: " + '/'.join(list(map(str, state))))

        #return

if __name__ == '__main__':
    play_the_game()
    play_the_game()
    play_the_game()