from collections import Counter
from dataclasses import dataclass
from itertools import zip_longest

@dataclass
class Point:
  x: int
  y: int

  def __hash__(self):
    return hash((self.x, self.y))

@dataclass
class Segment:
  a: Point
  b: Point

  def orthogonal(self):
    return self.a.x == self.b.x or self.a.y == self.b.y

  def points(self):
    x = (lambda step: list(range(self.a.x, self.b.x + step, step)))((-1, 1)[self.b.x >= self.a.x])
    y = (lambda step: list(range(self.a.y, self.b.y + step, step)))((-1, 1)[self.b.y >= self.a.y])
    return [(x, y) for x, y in zip_longest(x, y, fillvalue=(self.a.y, self.a.x)[len(x) == 1])]

def main(segments):
  # Part I
  c = Counter()
  for segment in list(filter(lambda s: s.orthogonal(), segments)):
    for point in segment.points():
      c[point] += 1
  print(f'Part 1: {len(list(filter(lambda k: c[k] > 1, c)))}')

  # Part II
  c = Counter()
  for segment in segments:
    for point in segment.points():
      c[point] += 1
  print(f'Part 2: {len(list(filter(lambda k: c[k] > 1, c)))}')

if __name__ == '__main__':
  main(
    list(
      map(
        lambda x:
        Segment(*list(map(lambda y: Point(*list(map(lambda z: int(z.strip()), y.split(',')))), x.split('->')))),
        open('input/5.txt').readlines()
      )
    )
  )
