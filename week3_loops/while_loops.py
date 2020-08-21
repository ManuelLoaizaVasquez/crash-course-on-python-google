def attempts(n):
  x = 1
  while x <= n:
    print("Attempt " + str(x))
    x += 1
  print("Done")

def count_down(start_number):
  current = start_number
  while current > 0:
    print(current)
    current -= 1
  print("Zero!")

def print_range(start, end):
  n = start
  while n <= end:
    print(n)
    n += 1

def print_prime_factors(number):
  factor = 2
  while factor <= number:
    if number % factor == 0:
      print(factor)
      number /= factor
    else:
      factor += 1
  return "Done"

def is_power_of_two(n):
  while n % 2 == 0:
    if n == 0:
      break
    n /= 2
  if n == 1:
    return True
  return False

def sum_divisors(n):
  sum = 0
  divisor = 1
  while divisor < n:
    if n % divisor == 0:
      sum += divisor
    divisor += 1
  return sum

def multiplication_table(number):
  multiplier = 1
  while multiplier <= 5:
    result = multiplier * number
    if result > 25:
      break
    print(str(number) + "x" + str(multiplier) + "=" + str(result))
    multiplier += 1

x = 0
while x < 5:
  print("Not there yet, x = " + str(x))
  x = x + 1
print("x = " + str(x))

attempts(5)
count_down(3)
print_range(1, 5)  # Should print 1 2 3 4 5 (each number on its own line)

print_prime_factors(100)
# Should print 2,2,5,5

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

multiplication_table(3) 
# Should print: 3x1=3 3x2=6 3x3=9 3x4=12 3x5=15
multiplication_table(5) 
# Should print: 5x1=5 5x2=10 5x3=15 5x4=20 5x5=25
multiplication_table(8)	
# Should print: 8x1=8 8x2=16 8x3=24