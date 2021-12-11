D = {')': '(', ']': '[', '}': '{', '>': '<'}
P = {')': 3, ']': 57, '}': 1197, '>': 25137}

class Stack:
  def __init__(self):
    self.__s = []

  def push(self, item):
    self.__s.append(item)

  def pop(self):
    if self.empty():
      return
    return self.__s.pop()

  def match(self, item):
    return D[item] == self.pop()

  def empty(self):
    return not len(self.__s)

def A(chunks):
  score = 0
  for chunk in chunks:
    S = Stack()
    for i, v in enumerate(chunk):
      if v in D.values():
        S.push(v)
        continue
      if v in D.keys() and not S.match(v):
        score += P[v]
        break
  return score

def B(chunks):
  pass

def main(chunks):
  print(f'Part 1: {A(chunks)}', f'Part 2: {B(chunks)}')

if __name__ == '__main__':
  main(list(map(lambda x: list(x.strip()), open('input/10.txt').readlines())))
