def show_letters(word):
  for letter in word:
    print(letter)

def digits(n):
  if n < 10:
    return 1
  return 1 + digits(n // 10)

def multiplication_table(start, stop):
  for x in range (start, stop + 1):
    for y in range (start, stop + 1):
      print(str(x * y), end = " ")
    print()

def counter(start, stop):
  x = start
  if x > stop:
    return_string = "Counting down: "
    while x >= stop:
      return_string += str(x)
      if x > stop:
        return_string += ","
      x -= 1
  else:
    return_string = "Counting up: "
    while x <= stop:
      return_string += str(x)
      if x < stop:
        return_string += ","
      x += 1
  return return_string

def even_numbers(maximum):
  return_string = ""
  for x in range (2, maximum + 1, 2):
    return_string += str(x) + " "
  return return_string.strip()

number = 1
while number <= 7:
  print(number, end = " ")
  number += 1

show_letters("Hello")

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

multiplication_table(1, 3)

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

for x in range(1, 10, 3):
  print(x)
for x in range(10):
  for y in range(x):
    print(y)
print(y)