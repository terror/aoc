import re

def main():
  d, p1, p2 = [i for i in open('input/4.txt').read().split("\n\n")], 0, 0
  for p in d:
    p1 += v(dict(x.split(":") for x in p.split()))
    p2 += vv(dict(x.split(":") for x in p.split()))
  print("Part 1: {}\nPart 2: {}".format(p1, p2))

def v(x):
  if all(map(lambda a: a in x, ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"))):
    return 1
  return 0

def vv(x):
  if not v(x):
    return 0
  if (
    920 <= int(x['byr']) <= 2002 and 2010 <= int(x['iyr']) <= 2020 and 2020 <= int(x['eyr']) <= 2030 and hgt(x['hgt'])
    and re.match(r'^[#][0-9a-f]{6}$', x['hcl']) and ecl(x['ecl']) and re.match(r'^\d{9}$', x['pid'])
  ):
    return 1
  return 0

def hgt(x) -> bool:
  if x[-2:] == 'in':
    return 59 <= int(x[:-2]) <= 76
  else:
    return 150 <= int(x[:-2]) <= 193

def ecl(x) -> bool:
  return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

if __name__ == '__main__':
  main()
