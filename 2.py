from util import *

source = grab_contents(2, "ocr")

char_count = {}
for char in source:
  char_count[char] = char_count.get(char, 0) + 1

print char_count
