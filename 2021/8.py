def A(lines):
  ans = 0
  for _, b in lines:
    ans += sum([len(item) in [2, 3, 4, 7] for item in b.split()])
  return ans

def B(lines):
  pass

def main(lines):
  print(f'Part 1: {A(lines)}', f'Part 2: {B(lines)}')

if __name__ == '__main__':
  main(list(map(lambda x: x.strip().split(' | '), open('input/8.txt').readlines())))
