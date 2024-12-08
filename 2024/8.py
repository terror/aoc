from math import gcd

grid = list(map(lambda x: list(x.strip()), open('input/8.txt')))

rows, cols = len(grid), len(grid[0])

def is_integer(n):
  return abs(n - round(n)) < 1e-12

antennas_by_freq = {}
for r in range(rows):
  for c in range(cols):
    ch = grid[r][c]
    if ch.isalnum():
      antennas_by_freq.setdefault(ch, []).append((r, c))

lambdas = [-1, 1/3, 2/3, 2]

antinodes_part1 = set()

for _, positions in antennas_by_freq.items():
  if len(positions) < 2:
    continue

  for i in range(len(positions)):
    A = positions[i]
    Ax, Ay = A
    for j in range(i+1, len(positions)):
      B = positions[j]
      Bx, By = B
      dx = Bx - Ax
      dy = By - Ay

      if dx == 0 and dy == 0:
        continue

      for lam in lambdas:
        Cx = Ax + lam * dx
        Cy = Ay + lam * dy
        if is_integer(Cx) and is_integer(Cy):
          Cx_int = int(round(Cx))
          Cy_int = int(round(Cy))
          if 0 <= Cx_int < rows and 0 <= Cy_int < cols:
            antinodes_part1.add((Cx_int, Cy_int))

print('Part 1:', len(antinodes_part1))

antinodes_part2 = set()

for freq, positions in antennas_by_freq.items():
  if len(positions) < 2:
    continue

  for i in range(len(positions)):
    A = positions[i]
    Ax, Ay = A
    for j in range(i+1, len(positions)):
      B = positions[j]
      Bx, By = B

      dx = Bx - Ax
      dy = By - Ay

      g = gcd(dx, dy)
      dxs = dx // g
      dys = dy // g

      n = 0
      while True:
        Cx = Ax + n * dxs
        Cy = Ay + n * dys
        if 0 <= Cx < rows and 0 <= Cy < cols:
          antinodes_part2.add((Cx, Cy))
          n += 1
        else:
          break

      n = -1
      while True:
        Cx = Ax + n * dxs
        Cy = Ay + n * dys
        if 0 <= Cx < rows and 0 <= Cy < cols:
          antinodes_part2.add((Cx, Cy))
          n -= 1
        else:
          break

print('Part 2:', len(antinodes_part2))
