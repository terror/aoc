from collections import Counter

x = [int(i) for i in open('input/10.txt').readlines()]
x.sort()
dp = [0] * (max(x) + 1)
dp[0] = 1
dp[1] = 1
dp[2] = 2

def main():
  lol = max(x)
  s, d = 0, Counter()
  for i in x:
    d[abs(s - i)] += 1
    s = i
  d[abs(s - (lol + 3))] += 1
  print("Part 1:", d[1] * d[3])
  print("Part 2:", go(dp, x))

def go(dp, x):
  x.append(0)
  x.sort()
  for i in x[3:]:
    for j in range(1, 4):
      dp[i] += dp[i - j]
  return dp[-1]

if __name__ == '__main__':
  main()
