x = [int(i) for i in open('input/9.txt', 'r').readlines()]

def ok(v, n):
  sums = []
  for i in range(v - 25, v):
    for j in range(v - 25, v):
      if i == j:
        continue
      sums.append(x[i] + x[j])
  return n in sums

def main():
  for i in range(25, len(x)):
    if not ok(i, x[i]):
      return x[i]

val = main()

def go():
  for i in range(len(x)):
    s = x[i]
    curr = [x[i]]
    for j in range(i + 1, len(x)):
      s += x[j]
      curr.append(x[j])
      if s == val:
        return min(curr) + max(curr)
      if s > val:
        continue

if __name__ == '__main__':
  print("Part 1:", val)
  print("Part 2:", go())
