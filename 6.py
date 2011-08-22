import re

nothing = 90052

for x in range(909):
  content = open("_6_txt/"+str(nothing)+".txt").read()
  nothing = re.sub('[^0-9]', '', content)
  try:
    int(nothing)
    print nothing
  except:
    print content
