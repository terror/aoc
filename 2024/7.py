from dataclasses import dataclass
from typing import List, Sequence
from itertools import product

@dataclass
class Equation:
  target: int
  numbers: List[int]

  @classmethod
  def parse(cls, line: str) -> 'Equation':
    target_str, numbers_str = line.strip().split(': ')

    return cls(
      target=int(target_str),
      numbers=[int(x) for x in numbers_str.split()]
    )

def evaluate_expression(numbers: Sequence[int], operators: Sequence[str]) -> int:
  result = numbers[0]

  for i, operator in enumerate(operators):
    next_num = numbers[i + 1]

    if operator == '+':
      result += next_num
    elif operator == '*':
      result *= next_num
    elif operator == '||':
      result = int(str(result) + str(next_num))

  return result

def solve_equation(eq: Equation, operators: List[str]) -> bool:
  operator_slots = len(eq.numbers) - 1

  for ops in product(operators, repeat=operator_slots):
    if evaluate_expression(eq.numbers, ops) == eq.target:
      return True

  return False

equations = []

with open('input/7.txt') as f:
  for line in f:
    if line.strip():
      equations.append(Equation.parse(line))

print(
  'Part 1:',
  sum(
    eq.target
    for eq in equations
    if solve_equation(eq, ['+', '*'])
  )
)

print(
  'Part 2:',
  sum(
    eq.target
    for eq in equations
    if solve_equation(eq, ['+', '*', '||'])
  )
)
