from collections import Counter

MXN = int(2e5) * 1000

def A(crabs):
  ans = MXN
  for k, _ in Counter(crabs).most_common():
    curr = 0
    for crab in crabs:
      curr += abs(crab - k)
    ans = min(curr, ans)
  return ans

def B(crabs):
  ans = MXN
  for k, _ in Counter(crabs).most_common():
    curr = 0
    for crab in crabs:
      n = abs(crab - k)
      curr += n * (n + 1) // 2
    ans = min(curr, ans)
  return ans

def main(crabs):
  print(f'Part 1: {A(crabs)}', f'Part 2: {B(crabs)}')

if __name__ == '__main__':
  main(list(map(int, open('input/7.txt').readlines()[0].split(','))))
