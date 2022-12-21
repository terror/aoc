O = {
  'A': 'R',
  'B': 'P',
  'C': 'S',
  'X': 'R',
  'Y': 'P',
  'Z': 'S'
}

P = {
  'P': 2,
  'R': 1,
  'S': 3
}

X = {
  'P': 'R',
  'R': 'S',
  'S': 'P'
}

W = {
  'P': 'S',
  'R': 'P',
  'S': 'R'
}

def eval(a, b):
  ret = 0

  match (a, b):
    case ('R', 'P') | ('S' ,'R') | ('P', 'S'):
      ret = 6
    case ('S', 'S') | ('R', 'R') | ('P', 'P'):
      ret = 3
    case ('P', 'R') | ('R', 'S') | ('S', 'P'):
      ret = 0

  return P[b] + ret

def reverse(a, b):
  ret = (0, 0)

  match (a, b):
    case ('R', 'P') | ('S' ,'P') | ('P', 'P'):
      ret = (3, P[a])
    case ('S', 'R') | ('R', 'R') | ('P', 'R'):
      ret = (0, P[X[a]])
    case ('P', 'S') | ('R', 'S') | ('S', 'S'):
      ret = (6, P[W[a]])

  return sum(ret)


(lambda lines: print(
  sum(map(lambda line: eval(*map(lambda x: O[x], line.split())), lines)),
  sum(map(lambda line: reverse(*map(lambda x: O[x], line.split())), lines))
))(list(map(lambda x: x.strip(), open('input/2.txt').readlines())))
