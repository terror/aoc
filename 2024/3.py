import re

text = open('input/3.txt').read().strip()

pattern = r"mul\((\d+),\s*(\d+)\)"

matches = re.findall(pattern, text)

print('Part 1:', sum(x * y for x, y in [(int(x), int(y)) for x, y in matches]))

pattern = r"mul\((\d+),\s*(\d+)\)|do\(\)|don't\(\)"

matches = re.finditer(pattern, text)

results = []

for m in matches:
  if m.group(0).startswith('mul'):
    results.append((int(m.group(1)), int(m.group(2))))
  else:
    results.append(m.group(0) == 'do()')

ans, curr = 0, True

for x in results:
  if isinstance(x, bool):
    curr = x
  else:
    if curr:
      a, b = x
      ans += a * b

print('Part 2:', ans)
