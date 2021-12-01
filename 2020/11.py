# tired boyz

grid = [list(i.strip()) for i in open('input/11.txt').readlines()]
R, C = len(grid), len(grid[0])
assert R == 90

def main():
  ans = 0
  p = 1
  while p:
    p ^= 1
    for i in range(R):
      for j in range(C):
        if grid[i][j] == 'L':
          if c(i, j):
            grid[i][j] = '#'
            p = 1
        if grid[i][j] == '#':
          if b(i, j):
            grid[i][j] = 'L'
            p = 1
    if p == 0:
      break

  for i in grid:
    for j in i:
      ans += j == '#'
  print(ans)

def c(i, j):
  if i - 1 >= 0:
    if grid[i - 1][j] == '#':
      return 0
  if i + 1 < R:
    if grid[i + 1][j] == '#':
      return 0
  if j - 1 >= 0:
    if grid[i][j - 1] == '#':
      return 0
  if i + 2 < R:
    if grid[i + 2][j] == '#':
      return 0
  if i + 2 < R and j + 1 < C:
    if grid[i + 2][j + 1] == '#':
      return 0
  if i + 1 < R and j + 2 < C:
    if grid[i + 1][j + 2] == '#':
      return 0
  if i + 2 < R and j + 2 < C:
    if grid[i + 2][j + 2] == '#':
      return 0
  return 1

def b(i, j):
  cnt = 0
  if i - 1 >= 0:
    cnt += grid[i - 1][j] == '#'
  if i + 1 < R:
    cnt += grid[i + 1][j] == '#'
  if j - 1 >= 0:
    cnt += grid[i][j - 1] == '#'
  if j + 1 < C:
    cnt += grid[i][j + 1] == '#'
  if j + 2 < C:
    cnt += grid[i][j + 2] == '#'
  if i + 2 < R and j + 1 < C:
    cnt += grid[i + 2][j + 1] == '#'
  if i + 1 < R and j + 2 < C:
    cnt += grid[i + 1][j + 2] == '#'
  if i + 2 < R and j + 2 < C:
    cnt += grid[i + 2][j + 2] == '#'
  return cnt >= 4

if __name__ == '__main__':
  main()
