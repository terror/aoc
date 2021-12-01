from collections import Counter

def main():
  # --- Part 1 ---
  print(
    "Part 1:",
    sum([
      len(set(filter(lambda x: x != '', [j.strip()
                                         for j in i])))
      for i in [i for i in open("input/6.txt").read().split("\n\n")]
    ])
  )

  # --- Part 2 ---
  ans = 0
  for i in [i for i in open("input/6.txt").read().split("\n\n")]:
    for k, v in Counter(list(filter(lambda x: x != '', [j.strip() for j in i]))).items():
      if v == len(i.split("\n")):
        ans += 1
  print("Part 2:", ans)

if __name__ == '__main__':
  main()
