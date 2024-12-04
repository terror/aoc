grid = list(map(lambda x: list(x.strip()), open('input/4.txt').readlines()))

rows, cols = len(grid), len(grid[0])

def safe_lookup(i: int, j: int) -> str:
  if i < 0 or i >= rows: return ''
  if j < 0 or j >= cols: return ''
  return grid[i][j]

def safe_lookup_many(positions) -> str:
  s = ''

  for i, j in positions:
    s += safe_lookup(i, j)

  return s

ans = set()

def look_xmas(i: int, j: int):
  positions = [
    [(i, j), (i, j - 1), (i, j - 2), (i, j - 3)],
    [(i, j), (i, j + 1), (i, j + 2), (i, j + 3)],
    [(i, j), (i - 1, j), (i - 2, j), (i - 3, j)],
    [(i, j), (i + 1, j), (i + 2, j), (i + 3, j)],
    [(i, j), (i - 1, j - 1), (i - 2, j - 2), (i - 3, j - 3)],
    [(i, j), (i - 1, j + 1), (i - 2, j + 2), (i - 3, j + 3)],
    [(i, j), (i + 1, j - 1), (i + 2, j - 2), (i + 3, j - 3)],
    [(i, j), (i + 1, j + 1), (i + 2, j + 2), (i + 3, j + 3)]
  ]

  for p in positions:
    if safe_lookup_many(p) in ['XMAS']:
      ans.add(tuple(p))

for i in range(len(grid)):
  for j in range(len(grid)):
    look_xmas(i, j)

print('Part 1:', len(ans))

ans = set()

def look_x_mas(i: int, j: int):
  positions = [
    ((i - 1, j - 1), (i + 1, j + 1)),
    ((i + 1, j - 1), (i - 1, j + 1)),
  ]

  if all(safe_lookup_many(p) in ['MS', 'SM'] for p in positions):
    ans.add(tuple(positions))

for i in range(len(grid)):
  for j in range(len(grid)):
    if grid[i][j] == 'A':
      look_x_mas(i, j)

print('Part 2:', len(ans))
