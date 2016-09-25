import re
import requests

def normalize(word):
	"""
	sorts the letter within a word in alphabetical order
	for easier comparison w/ scrambled words
	"""
	return ''.join(sorted(list(str(word))))


chall_url = "https://www.hackthissite.org/missions/prog/1/index.php"



def chall1():
	## step 1: build normalized word list
	f = open('wordlist.txt', 'r')

	words = []
	for line in f:
		words.append(line[:-1]) # removing trailing \n

	normalized = map(normalize, words)

	## step 2: retrieve challenge's word list
	html = requests.get(chall_url, headers = {"cookie": "__htsCookieNotice=1; PHPSESSID=jr6jjsqb3vlghagaka47p5n4h7"}).text

	chall_pattern = 'scrambled words((.*\n){10})' # first, get the block of html with the words
	block = re.search(chall_pattern, html, re.MULTILINE)

	block = block.group(0)
	block = block.split("\n")

	word_pattern = '<li>(.*)</li>' # then, extract the words from the block 
	
	chall_words = []
	for line in block:
		res = re.search(word_pattern, line)

		if res is not None and res.group(1):
			chall_words.append(res.group(1))

	print("Challenge (before normalization): " + str(', '.join(chall_words)))

	chall_words = map(normalize, chall_words)


	## step 3: find the unscrambled words
	solution = []
	for word in chall_words:
		solution.append(words[normalized.index(word)])

	solution = ','.join(solution)

	print("Solution found: " + solution)



	# step 4: submit solution
	finalOutcome = requests.post(chall_url, headers = {"cookie": "__htsCookieNotice=1; PHPSESSID=jr6jjsqb3vlghagaka47p5n4h7", "Referer": chall_url}, data = {"solution": solution}).text

	print(finalOutcome)

chall1();
