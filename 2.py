import os

if not os.path.isfile("_2.txt"):
	import urllib
	sock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
	source = sock.read().split("<!--")
	sock.close()
	source = source[2].replace("-->", "")
	f = open("_2.txt", "w")
	f.write(source)
	f.close()
else:
	f = open("_2.txt", "r")
	source = f.read()
	f.close()

char_count = {}
for char in source:
	char_count[char] = char_count.get(char, 0) + 1

print char_count
