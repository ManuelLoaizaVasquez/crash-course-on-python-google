def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n - 1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

def sum_positive_numbers(n):
  if n < 1:
    return 0
  return n + sum_positive_numbers(n - 1)

def is_power_of(number, base):
  if number == 1:
    return True
  if number < base:
    return False
  if number % base == 0:
    return is_power_of(number // base, base)
  else:
    return False

factorial(4)
factorial(10)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

print(sum_positive_numbers(3))
print(sum_positive_numbers(5))