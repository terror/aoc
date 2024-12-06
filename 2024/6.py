grid = list(map(lambda x: list(x.strip()), open('input/6.txt')))

rows, cols = len(grid), len(grid[0])

visited = set()

directions = {
  'v': (1, 0),
  '^': (-1, 0),
  '>': (0, 1),
  '<': (0, -1)
}

turn = {
  'v': '<',
  '^': '>',
  '>': 'v',
  '<': '^'
}

def simulate(x: int, y: int):
  curr_char = grid[x][y]
  # grid[x][y] = 'X'
  visited.add((x, y))

  while True:
    direction = directions[curr_char]
    nx, ny = x + direction[0], y + direction[1]

    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
      break

    if grid[nx][ny] == '#':
      curr_char = turn[curr_char]
      continue

    x, y = nx, ny
    visited.add((x, y))
    # grid[x][y] = 'X'

start_x = start_y = 0

for i in range(rows):
  for j in range(cols):
    if grid[i][j] not in ['.', '#', 'X']:
      start_x = i
      start_y = j
      simulate(i, j)

# for r in grid:
#   print(''.join(r))

print('Part 1:', len(visited))

ans = set()

def try_obstacle():
  states = set()
  x, y = start_x, start_y

  curr_char = grid[x][y]

  while True:
    state = (x, y, curr_char)

    if state in states:
      return True

    states.add((x, y, curr_char))

    direction = directions[curr_char]
    nx, ny = x + direction[0], y + direction[1]

    if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
      break

    if grid[nx][ny] == '#':
      curr_char = turn[curr_char]
      continue

    x, y = nx, ny

  return False

for i in range(rows):
  for j in range(cols):
    if (i, j) not in visited:
      continue
    if grid[i][j] == '.':
      grid[i][j] = '#'
      if try_obstacle():
        ans.add((i, j))
      grid[i][j] = '.'

print('Part 2:', len(ans))
