from collections import defaultdict
import typing as t

f = open('input/5.txt').read()

orderings, updates = list(map(lambda x: x.strip().split('\n'), f.split('\n\n')))

order_map = defaultdict(set)

for order in orderings:
  a, b = order.split('|')
  order_map[int(a)].add(int(b))

def is_update_good(update: t.List[int]):
  for i in range(len(update)):
    curr = update[i]
    if any(x in order_map[curr] for x in update[:i]):
      return False
  return True

ans = 0

print(updates)

incorrect_updates = []

for update in updates:
  curr_update = list(map(int, update.split(',')))
  if is_update_good(curr_update):
    middle = curr_update[len(curr_update) // 2]
    ans += middle
  else:
    incorrect_updates.append(curr_update)

print('Part 1:', ans)

ans = 0

def fix_update(update: t.List[int]) -> t.List[int]:
  for i in range(len(update)):
    for j in range(len(update)):
      if update[j] in order_map[update[i]]:
        update[i], update[j] = update[j], update[i]
  return update

for update in incorrect_updates:
  fixed = fix_update(update)
  middle = fixed[len(fixed) // 2]
  ans += middle

print('Part 2:', ans)
