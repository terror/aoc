input = open('input/1.txt')

l, r = [], []

for line in map(lambda x: x.strip(), input.readlines()):
  a, b = line.split()
  l.append(int(a))
  r.append(int(b))

l.sort()
r.sort()

ans = 0

for i in range(len(l)):
  ans += abs(l[i] - r[i])

print('Part 1:', ans)

ans = 0

for i in range(len(l)):
  ans += l[i] * r.count(l[i])

print('Part 2:', ans)
