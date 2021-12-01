def main():
  x = open('input/13.txt').readlines()
  _id = w = int(x[0].strip())
  x[1], p, t, d = x[1].split(","), 0, 0, 1
  for i in range(len(x[1])):
    if x[1][i] != 'x':
      x[1][i] = int(x[1][i])
  while 1:
    for i in range(len(x[1])):
      if x[1][i] == 'x':
        continue
      if w % x[1][i] == 0:
        print("Part 1:", (w - _id) * (x[1][i]))
        p = 1
    if p:
      break
    w += 1
  for o, b in [(o, b) for o, b in enumerate(x[1]) if b != 'x']:
    while t % b != (b - (o % b)) if o else 0:
      t += d
    d *= b
  print("Part 2:", t)

if __name__ == '__main__':
  main()
