import os
import urllib

def grab_contents(challenge, url):
  challenge = str(challenge)
  if not os.path.isfile("_"+challenge+".txt"):
    sock = urllib.urlopen("http://www.pythonchallenge.com/pc/def/"+url+".html")
    source = sock.read().split("<!--")
    sock.close()
    if len(source) > 2:
      source = source[2].replace("-->", "")
    else:
      source = source[1].replace("-->", "")
    f = open("_"+challenge+".txt", "w")
    f.write(source)
    f.close()
  else:
    f = open("_"+challenge+".txt", "r")
    source = f.read()
    f.close()
  return source
