from sparrow6lib import *

x = 0
y = 0
lines = 0
for line in config()['lines']:
  items = line.strip().split(",")
  x += float(items[0])
  y += float(items[1])
  lines += 1
print("avg: %s - %s" % ( x/lines, y/lines ))
