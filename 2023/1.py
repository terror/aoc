import typing as t

f = list(map(lambda x: x.strip(), open('input/1.txt').readlines()))

def get_digits(s: str) -> t.List[str]:
  ret = []
  for x in s:
    if x.isdigit():
      ret.append(int(x))
  return ret

ans = 0

d = {
  'one': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight':8,
  'nine': 9,
}

overlaps = {
  'eighthree': 'eight$hree',
  'eightwo': 'eight$wo',
  'fiveeight': 'five$ight',
  'nineight': 'nine$ight',
  'oneight': 'one$ight',
  'sevenine': 'seven$ine',
  'threeight': 'three$ight',
  'twone': 'two$ne',
}

def process(s):
  for overlap, r in overlaps.items():
    if overlap in s:
      s = s.replace(overlap, r)
  for word, num in d.items():
    s = s.replace(word, str(num))
  return s

for x in list(map(lambda x: process(x), f)):
  digits = get_digits(x)
  ans += int(str(digits[0]) + str(digits[0])) if len(digits) == 1 else int(str(digits[0]) + str(digits[-1]))

print(ans)
