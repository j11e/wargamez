import requests
import re
import urllib.parse

def chall():
	chall_url = 'https://www.hackthissite.org/missions/prog/12/index.php';
	cookie = "__utma=198402870.689107361.1470243770.1470243770.1470243770.1; __utmc=198402870; __utmz=198402870.1470243770.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __htsCookieNotice=1; PHPSESSID=limseb5euijunvvih7sbpk4i62; style_cookie=printonly"
	headers = {"Cookie": cookie, "Referer": chall_url}

	html = requests.get(chall_url, headers={"Cookie": cookie}).text

	if "developer" in html:
		print(html)

	html = re.search('String: </b><input type="text" value="([^"]*)"', html).group(1)

	print("Whole string is " + html)

	composite_numbers = []
	prime_numbers = []
	non_numeric = []
	for char in html:
		if char in '4689':
			composite_numbers.append(int(char))
		elif char in '2357':
			prime_numbers.append(int(char))
		elif char not in '01':
			non_numeric.append(char)

	sum_composite = 0
	for number in composite_numbers:
		sum_composite += number

	sum_prime = 0
	for number in prime_numbers:
		sum_prime += number

	res = sum_prime * sum_composite

	first_chars = non_numeric[:25]
	first_chars = [chr(ord(char) + 1) for char in first_chars]

	solution = ''.join(first_chars) + str(res)

	print("Solution is " + solution)

	# solution = urllib.parse.quote_plus(solution)

	result = requests.post(chall_url, headers={"Cookie": cookie, "Referer": chall_url}, data={"solution": solution, "submitbutton": "Submit"}).text

	print(result)


chall()






