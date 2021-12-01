def main():
  acc, I = 0, [i.split() for i in open('input/8.txt', 'r').readlines()]
  print("Part 1:", go(I)[0])
  print("Part 2:", p2(I))

def p2(I):
  for i in range(len(I)):
    a, b = I[i]
    if a == "nop":
      I[i][0] = "jmp"
      res = go(I)
      if res[1]:
        return res[0]
      else:
        I[i][0] = "nop"
    if a == "jmp":
      I[i][0] = "nop"
      res = go(I)
      if res[1]:
        return res[0]
      else:
        I[i][0] = "jmp"
  return "something broke oof"

def go(I):
  vis, acc, idx = set(), 0, 0
  while True:
    if idx >= len(I):
      break
    a, b = I[idx][0], I[idx][1]
    x, o = int(b[1:]), b[0]
    if a == "acc":
      acc += x if o == "+" else -x
      idx += 1
    if a == "nop":
      idx += 1
    if a == "jmp":
      idx += x if o == "+" else -x
    if idx in vis:
      return (acc, 0)
    vis.add(idx)
  return (acc, 1)

if __name__ == '__main__':
  main()
