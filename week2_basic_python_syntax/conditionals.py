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

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

def format_name(first_name, last_name):
  string = "Name: "
  if len(first_name) == 0 and len(last_name) == 0:
    return ""
  elif len(first_name) == 0:
    string = string + last_name
  elif len(last_name) == 0:
    string = string + first_name
  else:
    string = string + last_name + ", " + first_name
  return string

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

def fractional_part(numerator, denominator):
  if denominator == 0:
    return 0
  return numerator / denominator - numerator // denominator

def sum(x, y):
  return (x + y)

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

print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("big" > "small")

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

print(((10 >= 5 * 2) and (10 <= 5 * 2)))

print(sum(sum(1, 2), sum(3, 4)))

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0