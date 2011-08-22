import pickle, urllib
import sys

sock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
data = pickle.load(sock)
sock.close()

for text in data:
  for content in text:
    sys.stdout.write(content[0] * content[1])
  print "\r"
