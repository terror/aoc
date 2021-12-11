class Grid:
  def __init__(self, grid):
    self.grid = grid
    self.rows = len(grid)
    self.columns = len(grid[0])

  def get(self, x, y):
    return int(self.grid[x][y])

def A(grid):
  ans = 0
  for r in range(grid.rows):
    for c in range(grid.columns):
      ans += (grid.get(r, c) + 1) * (
        not any([
          r - 1 >= 0 and grid.get(r - 1, c) <= grid.get(r, c), r + 1 < grid.rows
          and grid.get(r + 1, c) <= grid.get(r, c), c - 1 >= 0 and grid.get(r, c - 1) <= grid.get(r, c),
          c + 1 < grid.columns and grid.get(r, c + 1) <= grid.get(r, c)
        ])
      )
  return ans

def B(grid):
  pass

def main(grid):
  print(f'Part 1: {A(grid)}', f'Part 2: {B(grid)}')

if __name__ == '__main__':
  main(Grid(list(map(list, map(lambda x: x.strip(), open('input/9.txt').readlines())))))
