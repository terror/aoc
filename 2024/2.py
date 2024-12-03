f = open('input/2.txt', 'r')

reports = list(map(lambda x: list(map(int ,x.strip().split())), f.readlines()))

ans = 0

def is_safe(report: list[int]) -> bool:
  is_sorted = report == sorted(report) or report == sorted(report, reverse=True)

  does_differ = True

  for i in range(1, len(report)):
    if not 1 <= abs(report[i] - report[i - 1]) <= 3:
      does_differ = False
      break

  return is_sorted and does_differ

for report in reports:
  ans += is_safe(report)

print('Part 1:', ans)

ans = 0

for report in reports:
  if is_safe(report):
    ans += 1
    continue

  for i in range(len(report)):
    new_report = list(map(lambda x: x[1], filter(lambda x: x[0] != i, enumerate(report))))
    if is_safe(new_report):
      ans += 1
      break

print('Part 2:', ans)
