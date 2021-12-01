def main():
  ans = 0
  for line in open('input/2.txt', 'r').readlines():
    a, b, c = map(str, line.split())

    a = a.split("-")

    l, r = int(a[0]), int(a[1])
    """
        if solve(c, l, r, b[0]):
            ans += 1
        """
    if solve_p2(c, l, r, b[0]):
      ans += 1

  print(ans)

def solve(pw, l, r, c):
  return pw.count(c) >= l and pw.count(c) <= r

def solve_p2(pw, l, r, c):
  return pw[l - 1] == c and pw[r - 1] != c or (pw[l - 1] != c and pw[r - 1] == c)

if __name__ == '__main__':
  main()
