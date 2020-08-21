def square(n):
  return n * n

def sum_squares(x):
  sum = 0
  for n in range(x):
    sum += square(n)
  return sum

def factorial(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result

def to_celsius(x):
  return (x - 32) * 5 / 9

for x in range(5):
  print(x)

print(sum_squares(10))

values = [23, 52, 59, 37, 48]
sum = 0
length = 0
for value in values:
  sum += value
  length += 1
average = sum / length
print(average)

print(factorial(4))
print(factorial(10))

for x in range(0, 101, 10):
  print(to_celsius(x))

for left in range(6):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end = "")
  print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

for x in range(1, 11):
  print(x**3)

for x in range (0, 101):
  result = x * 7
  if result > 100:
    break
  print(result)