from dataclasses import dataclass

@dataclass
class Range:
  s: int
  e: int

  def contains(self, other):
    return self.s >= other.s and self.e <= other.e

  def overlaps(self, other):
    return len(set.intersection(set(range(self.s, self.e + 1)), set(range(other.s, other.e + 1)))) != 0

def eval(ranges, flag):
  tot = 0
  for a, b in ranges:
    tot += (a.contains(b) or b.contains(a), a.overlaps(b) or b.overlaps(a))[flag]
  return tot

ranges = list(
  map(
    lambda line:
    (lambda x: [Range(*map(int, x[0].split('-'))), Range(*map(int, x[1].split('-')))])(line.split(',')),
    list(map(lambda x: x.strip(),
             open('input/4.txt').readlines()))
  )
)

print(eval(ranges, 0), eval(ranges, 1))
