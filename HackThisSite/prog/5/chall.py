import requests
import commands

def chall():
	chall_url = "https://www.hackthissite.org/missions/prog/5/index.php"

	cookie = "__utma=198402870.689107361.1470243770.1470243770.1470243770.1; __utmc=198402870; __utmz=198402870.1470243770.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __htsCookieNotice=1; PHPSESSID=limseb5euijunvvih7sbpk4i62; style_cookie=printonly"
	headers = {"Cookie": cookie, "Referer": chall_url}

	corrupted = open(r"C:\Users\JD\Downloads\corrupted.png.bz2", 'rb').read()
	# whatevs

	# print(corrupted)

	start_marker = bytes.fromhex('314159265359')
	end_marker = bytes.fromhex('177245385090')

	try:
		print("input length: %d; index of start marker: %d; index of end marker: %d" % (len(corrupted), corrupted.index(start_marker), corrupted.index(end_marker)))
	except:
		print("No start or end marker found, let's not even waste time")
		return

	print("Number of \\r\\n pairs: %d" % (corrupted.count(b'\r\n')))

	pieces = corrupted.split(b'\r\n')

	# replace some of the \r\n with \n... try to decompress... rinse & repeat
	counter = 0

	while True:
		counter += 1


		output = commands.getstatusoutput("bunzip2 attempt.png.bz2")[1]
		if 'corrupted' not in output:
			print("Success! Final file is fixed.png")
			return

	# result = requests.post(chall_url, headers={"Cookie": cookie, "Referer": chall_url}, data={"solution": solution, "submitbutton": "Submit"}).text
	# print(result)




chall()



