import urllib
import re

nothing = 12345 
base_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

for x in range(400):
  content = urllib.urlopen(base_url+str(nothing)).read()
  nothing = re.sub('[^0-9]', '', content)
  try:
    int(nothing)
    print nothing
  except:
    print content
