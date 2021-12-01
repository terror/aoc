import re

d, lol, s = {}, {}, "shiny gold"

def go(x):
  for i in d[x]:
    if i == s or go(i):
      return 1
  return 0

def go2(x):
  return sum([int(i[0]) * (go2(i[1]) + 1) for i in lol[x]])

def main():
  for i in open('input/7.txt').readlines():
    x = re.findall(r'^(.+) bags contain (.+)$', i)
    d[x[0][0]] = re.findall(r'\d ([\w\s]+) bag', x[0][1])
    lol[x[0][0]] = re.findall(r'(\d+) ([\w\s]+) bag', x[0][1])

  print("Part 1:", sum([go(x) for x in d]))
  print("Part 2:", go2(s))

if __name__ == '__main__':
  main()
