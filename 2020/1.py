from itertools import combinations

def main():
  d = [int(i) for i in open('input/1.txt', 'r').readlines()]
  for i in combinations(d, 3):
    a, b, c = i
    if sum((a, b, c)) == 2020:
      return a * b * c

if __name__ == '__main__':
  print(main())
