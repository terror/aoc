class Board:
  def __init__(self, nums):
    self.nums = self.__construct(nums)
    self.R = len(nums)
    self.C = len(nums[0])
    self.has_won = False

  def __str__(self):
    ret = ""
    for i in range(self.R):
      for j in range(self.C):
        a, b = self.nums[i][j]
        ret += str(a) + " "
      ret += "\n"
    return ret

  def __construct(self, nums):
    return list(map(lambda x: list(map(lambda y: (int(y), False), x)), nums))

  def update(self, n):
    for i in range(self.R):
      for j in range(self.C):
        a, b = self.nums[i][j]
        if a == n:
          self.nums[i][j] = (a, True)

  def is_winner(self):
    for i in range(self.R):
      if all(list(map(lambda x: x[1], self.nums[i]))):
        return True

    columns = list(zip(*self.nums))
    for i in range(self.C):
      if all(list(map(lambda x: x[1], columns[i]))):
        return True

    return False

  def unmarked(self):
    ret = 0
    for i in range(self.R):
      for j in range(self.C):
        ret += self.nums[i][j][0] * (not self.nums[i][j][1])
    return ret

def main(lines):
  numbers = list(lines[0].split(','))

  # Gather boards
  boards = []
  curr = []
  for line in lines[2:]:
    if line == '':
      boards.append(Board(curr))
      curr = []
      continue
    curr.append(line.split())
  boards.append(Board(curr))

  store = []
  for number in numbers:
    for board in boards:
      board.update(int(number))
      if board.is_winner() and not board.has_won:
        board.has_won = True
        store.append((board.unmarked(), int(number)))

  first, last = store[0], store[-1]
  print(f'Part 1: {first[0] * first[1]}', f'Part 2: {last[0] * last[1]}')

if __name__ == '__main__':
  main(list(map(lambda x: x.strip(), open('input/4.txt').readlines())))
