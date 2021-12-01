def A(L):
  ans = 0
  for i in range(1, len(L)):
    ans += L[i] > L[i - 1]
  return ans

def B(L):
  ans = 0
  for i in range(1, len(X := [sum(L[i:i + 3]) for i in range(len(L))])):
    ans += X[i] > X[i - 1]
  return ans

if __name__ == '__main__':
  L = list(map(int, open('input/1.txt', 'r').readlines()))
  print(f'Part 1: {A(L)}', f'Part 2: {B(L)}')
