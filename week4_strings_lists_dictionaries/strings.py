def double_word(word):
  word = word + word
  return word + str(len(word))

def first_and_last(message):
  if len(message) == 0:
    return True
  return message[0] == message[-1]

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

def initials(phrase):
  words = phrase.upper().split()
  result = ""
  for word in words:
    result += word[0]
  return result

def student_grade(name, grade):
  return "{} received {}% on the exam".format(name, grade)

def to_celsius(x):
  return (x - 32) * 5 / 9

def is_palindrome(input_string):
  new_string = ""
  reverse_string = ""
  for letter in input_string:
    if letter != " ":
      new_string = new_string + letter.lower()
      reverse_string = letter.lower() + reverse_string
  return new_string == reverse_string

def convert_distance(miles):
  km = miles * 1.6
  result = "{} miles equals {:.1f} km".format(miles, km)
  return result

def nametag(first_name, last_name):
  return  "{} {}.".format(first_name, last_name[0])

def replace_ending(sentence, old, new):
  if sentence.endswith(old):
    new_sentence = sentence[:-len(old)] + new
    return new_sentence
  return sentence

# Concatenation
name = "Sasha"
color = 'gold'
print("Name: " + name + " , Favorite color: " + color)

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0

name = "Jaylen"
print(name[0])
print(name[1])
print(name[len(name) - 1])
print(name[-1])

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

# slice : substring
color = "Orange"
print(color[1 : 4])
fruit = "Pineapple"
print(fruit[: 4])
print(fruit[4 :])

message = "A kong string with a silly typo"
new_message = message[: 2] + "l" + message[3 :]
print(new_message)

# index
pets = "Cats & Dogs"
print(pets.index("&"))
print(pets.index("C"))
print(pets.index("Dog"))
print(pets.index("s"))

# upper y lower
print("Mountains".upper())
print("Mountains".lower())

# strip
print(" yes ".strip())
print(" yes ".lstrip())
print(" yes ".rstrip())

# count
print("The number of times e occurs in this string is 4".count("e"))

# endswith
print("Forest".endswith("rest"))

# isnumeric
print("Forest".isnumeric())
print("12345".isnumeric())

print(int("123") + int("456"))

# join
print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
print("...".join(["This", "is", "a", "phrase", "joined", "by", "triple", "dots"]))

# split
print("This is another example".split())

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

name = "Manny"
number = len(name) * 3
print("Hello, {}, your lucky number is {}.".format(name, number))
print("Your lucky number is {number}, {name}.".format(name = name, number = len(name) * 3))

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print("Base proce: ${:.2f}. With tax: ${:.2f}".format(price, with_tax))

for x in range(0, 101, 10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

weather = "Rainfall"
print(weather[:4])

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G."

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"