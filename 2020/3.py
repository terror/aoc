def p1(grid):
  ans = 0
  for i in range(len(grid)):
    ans += grid[i][3 * i % len(grid[0])] == '#'
  return ans

def p2(grid):
  a = b = c = d = e = 0
  for i in range(len(grid)):
    a += grid[i][i % len(grid[0])] == '#'
    b += grid[i][3 * i % len(grid[0])] == '#'
    c += grid[i][5 * i % len(grid[0])] == '#'
    d += grid[i][7 * i % len(grid[0])] == '#'

  for i in range(len(grid) // 2):
    e += grid[2 * i][i % len(grid[0])] == '#'

  return a * b * c * d * e

if __name__ == '__main__':
  grid = [list(line.rstrip()) for line in open('input/3.txt').readlines()]
  print("Part 1:", p1(grid))
  print("Part 2:", p2(grid))
