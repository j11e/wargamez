import re
import requests


dictionary = {}

url1 = "https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/prog_1.php"
url1_rep = "https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/verif_1.php"
url2 = "https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/prog_2.php"
url2_rep = "https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/verif_2.php"
url3 = "https://www.newbiecontest.org/epreuves/prog/frok-fichus_nb/prog_3.php"

cookies = {
    "PHPSESSID": "0f5a68209c4d3306a80b40f70536937f",
    "SMFCookie89": "a%3A4%3A%7Bi%3A0%3Bs%3A5%3A%2266929%22%3Bi%3A1%3Bs%3A40%3A%228aa08e09e0976cb352be5a6eff657591f1b75e5e%22%3Bi%3A2%3Bi%3A1705080948%3Bi%3A3%3Bi%3A0%3B%7D"
}


def load_dictionary():
    """two strings are anagrams if the "sorted strings" (same chars, but sorted)
    are equal. So: store all numbers in anag.txt, indexed by "sorted" version
    """
    f = open("/home/jd/anag.txt")
    for line in f:
        line = line.strip()
        key = ''.join(sorted(list(line)))
        if key in dictionary:
            print("! MULTIPLE ANAGRAMS!")
        dictionary[key] = line
    f.close()


def get_anagram_from_dict(string):
    sorted_string = ''.join(sorted(list(string)))
    if sorted_string in dictionary:
        return dictionary[sorted_string]
    return ""


def do_page_1():
    load_dictionary()

    r = requests.get(url1, cookies=cookies)
    raw = r.text.split("ordre sont: ")[1].split("<br")[0]
    numbers = re.split(r'[^0-9]', raw)
    numbers = list(filter(lambda x: len(x) > 0, numbers))

    anags = []
    for number in numbers:
        anags.append(get_anagram_from_dict(number))

    print("Numbers: %s "  % ", ".join(numbers))
    print("Anags: %s "  % ", ".join(anags))

    payload = {
        "rep1": anags[0],
        "rep2": anags[1],
        "rep3": anags[2],
        "rep4": anags[3],
        "rep5": anags[4],
        "rep6": anags[5],
        "rep7": anags[6]
    }

    r = requests.post(url1_rep, cookies=cookies, data=payload)
    login = r.text.split("e login est: ")[1].split(".")[0]
    print("Phase 1 login: %s" % login)

    return login

def do_page_2():
    print("Starting page 2.")

    r = requests.get(url2, cookies=cookies)
    second_question = int(r.text.split("s pour enlever ")[1].split(" ")[0])
    third_question = int(r.text.split("durant la ")[1][:3])

    # 1st question never changes: pre-calculate (good: cares about order, is slow to calculate)
    # the rest doesn't care about order of abduction: it's simply 2 fibonacci seqs
    first_answer = ['H', 381966012, 618033988]
    second_answer = 0
    third_answer = 0

    year = 2
    abductions_f = [0, 0, 1]
    abductions_m = [0, 1, 0]
    total = 2

    stop = False
    while not stop:
        year += 1

        abductions_f.append(abductions_f[-1] + abductions_f[-2])
        abductions_m.append(abductions_m[-1] + abductions_m[-2])


        # prevent excessive growth
        abductions_f = abductions_f[1:]
        abductions_m = abductions_m[1:]

        total += abductions_f[-1] + abductions_m[-1]

        if total >= second_question and second_answer == 0:
            second_answer = year
        
        if year == third_question:
            third_answer = abductions_f[-1] + abductions_m[-1]
    
        if second_answer != 0 and third_answer != 0:
            stop = True

    print("Questions: years to abduct %d people, number of abductees in year #%d" % (second_question, third_question))
    print("answers: %s %d %d %d %d" % (first_answer[0], first_answer[1], first_answer[2], second_answer, third_answer))

    payload = {
        "rep1": first_answer[0],
        "rep2": first_answer[1],
        "rep3": first_answer[2],
        "rep4": second_answer,
        "rep5": third_answer
    }
    r = requests.post(url2_rep, cookies=cookies, data=payload)
    password = r.text.split("e pass est: ")[1].split(".")[0]

    print("Phase 2 password: %s" % password)
    return password


def do_page_3(login, pwd):
    r = requests.post(url3, cookies=cookies, data={"login": login, "pass": pwd})
    print("Final challenge response: %s" % r.text)


if __name__ == "__main__":
    login = do_page_1()
    pwd = do_page_2()

    do_page_3(login, pwd)
