import re, zipfile, sys

nothing = 90052
ids = [nothing]

z = zipfile.ZipFile("channel.zip", "r")

for x in range(909):
  content = z.read(str(nothing)+".txt")
  nothing = re.sub('[^0-9]', '', content)
  try:
    int(nothing)
    print nothing
    ids.append(nothing)
  except:
    print content


for i in ids:
  sys.stdout.write(z.getinfo("%s.txt" % i).comment)
