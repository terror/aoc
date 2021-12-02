from enum import Enum

L = tuple(map(lambda x: x.split(), open('./input/2.txt').readlines()))

class OP(Enum):
  F = 0
  D = 1
  U = 2

  def __str__(self):
    return {0: 'forward', 1: 'down', 2: 'up'}[self.value]

def F(T):
  return sum(map(lambda x: int(x[1]), filter(lambda x: x[0] == str(T), L)))

def A():
  return F(OP.F) * (-F(OP.U) + F(OP.D))

def B():
  a = d = 0
  for pos, x in L:
    a += (pos == 'down') * int(x) - (pos == 'up') * int(x)
    d += (pos == 'forward') * (int(x) * a)
  return F(OP.F) * d

if __name__ == '__main__':
  print(f'Part 1: {A()}', f'Part 2: {B()}')
