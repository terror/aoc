from collections import Counter

def main(state, days=256, age=9):
  for i in range(days):
    c = 0
    for j in range(age):
      # 0 -> reproduce
      # Accumulate how many 0's we have
      if not j:
        c += state[j]
        state[7] += state[j]
      # 'Subtract' one from each age by shifting down
      else:
        state[j - 1] = state[j]
    state[8] = c
  print(sum(state.values()))

if __name__ == '__main__':
  main(Counter(list(map(int, open('input/6.txt').readlines()[0].split(',')))))
