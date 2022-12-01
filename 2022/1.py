(lambda sums: print(max(sums), sum(sorted(sums, reverse=True)[:3])))(
  list(map(lambda x: sum(map(lambda y: int(y), x.split('\n'))),
           open('input/1.txt').read().strip().split('\n\n')))
)
