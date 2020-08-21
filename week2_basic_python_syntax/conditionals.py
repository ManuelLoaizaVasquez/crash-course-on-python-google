def hint_username(username):
  if len(username) < 3:
    print("Invalid username. Must be at least 3 characters long")
  elif len(username) > 15:
    print("Invalid username. Must be at most 15 characters long")
  else:
    print("Valid username")

def is_positive(number):
  if number > 0:
    return True
  else:
    return False

def is_even(number):
  if number % 2 == 0:
    return True
  return False

def number_group(number):
  if number > 0:
    return "Positive"
  elif number == 0:
    return "Zero"
  else:
    return "Negative"

def greeting(name):
  if name == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

def check(number):
  if number > 11:
    print(0)
  elif number != 10:
    print(1)
  elif number >= 20 or number < 12:
    print(2)
  else:
    print(3)

def calculate_storage(filesize):
  block_size = 4096
  full_blocks = filesize // block_size
  partial_block_remainder = filesize % block_size
  if partial_block_remainder > 0:
    return (full_blocks + 1) * block_size
  return full_blocks * block_size

# boolean : uno de los dos posibles estados, verdadero o falso
print(10 > 1)
# equality operator
print("cat" == "dog")
print(1 != 2)
# print(1 < "1")
print(1 == "1")
print("cat" > "Cat")
print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25 > 50 or 1 != 2)
print(not 42 == "Answer")

print(number_group(10))
print(number_group(0))
print(number_group(-5))

print(greeting("Taylor"))
print(greeting("John"))

check(10)

print("A dog" < "A mouse")
print((9999 + 8888) < (100 * 100))

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192