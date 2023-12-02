f = list(map(lambda x: x.strip(), open('input/2.txt', 'r').readlines()))

ans = 0

for x in f:
  game_id = x.split(':')[0].split(' ')[1]
  rest = list(map(lambda x: x.strip(), x.split(':')[1:][0].split(';')))
  # works = True
  maxes = {'red': 0, 'blue': 0, 'green': 0}
  for item in rest:
    colors = list(map(lambda x: x.strip(), item.split(',')))
    scores = {'red': 0, 'blue': 0, 'green': 0}
    for y in colors:
      score, color = y.split(' ')
      scores[color] += int(score)
    # if scores['red'] > 12 or scores['blue'] > 14 or scores['green'] > 13:
    #   works = False
    #   break
    maxes['red'] = max(scores['red'], maxes['red'])
    maxes['blue'] = max(scores['blue'], maxes['blue'])
    maxes['green'] = max(scores['green'], maxes['green'])
  ans += (maxes['red'] * maxes['blue'] * maxes['green'])

print(ans)
