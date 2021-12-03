from collections import Counter

L = list(map(list, map(lambda x: x.strip(), open('input/3.txt').readlines())))

def A():
  a = b = ""
  for i in range(len(L[0])):
    c = Counter([R[i] for R in L])
    a += c.most_common()[0][0]
    b += c.most_common()[-1][0]
  return int(a, 2) * int(b, 2)

def B():
  X = L
  for i in range(len(L[0])):
    c = Counter([R[i] for R in X]).most_common()
    a, b = c[0], c[-1]
    p = '1' if a[1] == b[1] else a[0]
    X = list(filter(lambda x: x[i] == p, X))
  A = "".join(X[0])

  X = L
  for i in range(len(L[0])):
    c = Counter([R[i] for R in X]).most_common()
    if len(c) == 1:
      break
    a, b = c[0], c[-1]
    p = '0' if a[1] == b[1] else b[0]
    X = list(filter(lambda x: x[i] == p, X))
  B = "".join(X[0])

  return int(A, 2) * int(B, 2)

if __name__ == '__main__':
  print(f'Part 1: {A()}', f'Part 2: {B()}')
