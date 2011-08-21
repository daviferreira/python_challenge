import re
import sys
from util import *

source = grab_contents(3, "equality")

for m in re.finditer("[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", source):
  sys.stdout.write(m.group(1))