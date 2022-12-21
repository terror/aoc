import string

(
  lambda lines, P: print(
    sum(
      map(
        lambda item: sum(
          map(lambda x: P.index(x) + 1, set.intersection(set(item[:len(item) // 2]), set(item[len(item) // 2:])))
        ), lines
      )
    ),
    sum(
      map(
        lambda group: sum(map(lambda x: P.index(x) + 1, set.intersection(*map(lambda item: set(item), group)))),
        [lines[i:i + 3] for i in range(0, len(lines), 3)]
      )
    )
  )
)(
  list(map(lambda x: x.strip(),
           open('input/3.txt').readlines())), list(string.ascii_lowercase + string.ascii_uppercase)
)
