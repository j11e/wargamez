import requests
import re

def chall():
	chall_url = 'https://www.hackthissite.org/missions/prog/11/index.php';
	cookie = "__utma=198402870.689107361.1470243770.1470243770.1470243770.1; __utmc=198402870; __utmz=198402870.1470243770.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __htsCookieNotice=1; PHPSESSID=limseb5euijunvvih7sbpk4i62; style_cookie=printonly"

	html = requests.get(chall_url, headers={"Cookie": cookie}).text

	# print(html)

	cipher = re.search("Generated String: ([^<]*)", html).group(1)
	
	key = re.search("Shift: ([^<]*)", html).group(1)
	key = int(key)

	print("Need to rotate %s by %d chars" % (cipher, key))

	# solution = ''
	# for letter in cipher:
	# 	solution += chr(ord(letter) + key)

	# print("Result is " + solution + " with dumb shift")

	# result = requests.post(chall_url, headers={"Cookie": cookie, "Referer": chall_url}, data={"solution": solution}).text

	# print(result)

	# return 
	numbers = re.compile("[^0-9]").split(cipher)
	numbers = list(filter(lambda x: x != '', numbers))

	solution = ''.join([chr(int(value)-key) for value in numbers])

	print("Result is " + solution + " with number split")

	result = requests.post(chall_url, headers={"Cookie": cookie, "Referer": chall_url}, data={"solution": solution}).text

	print(result)


def chall2():
	t = "63,64,71,56,66,62,77,39,74,79,59,"
	solution = ''
	for letter in t:
		solution += chr(ord(letter) - 4)

	print(solution)


chall()

