from typing import List

def main():
  ans, ans2, s = 0, 0, []
  for i in [i for i in open('input/5.txt').readlines()]:
    x = int((i[:7].replace("F", "0").replace("B", "1")), 2) * 8 \
        + int(i[7:].replace("L", "0").replace("R", "1"), 2)
    ans = max(ans, x)
    s.append(x)
    ans2 = max(ans2, row(i[:7]) * 8 + col(i[7:]))

  print("Part 1 Type conversion:", ans)
  print("Part 1 Binary Search: ", ans2)

  s.sort()
  print("Part 2:", *[s[i] - 1 for i in range(1, len(s)) if s[i - 1] != s[i] - 1])

"""
An alternative approach to Part 1: Use binary search
"""

R, C = 127, 7

def row(s: List[str]) -> int:
  lo, hi, idx = 0, R, 0
  while lo <= hi:
    mid = (lo + hi) // 2
    if idx == len(s) - 1:
      if s[idx] == 'F':
        return mid - 1
      else:
        return mid + 1
    if s[idx] == 'F':
      hi = mid - 1
    else:
      lo = mid + 1
    idx += 1

def col(s: List[str]) -> int:
  lo, hi, idx = 0, C, 0
  while lo <= hi:
    mid = (lo + hi) // 2
    if s[idx] == 'L':
      hi = mid - 1
    else:
      lo = mid + 1
    idx += 1
  return mid

if __name__ == '__main__':
  main()
