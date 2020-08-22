def get_word(sentence, n):
  if n > 0:
    words = sentence.split(" ")
    if n <= len(words):
      return words[n - 1]
  return ""

def skip_elements(elements):
  new_list = []
  for index, element in enumerate(elements):
    if index % 2 == 0:
      new_list.append(element)
  return new_list

def convert_seconds(seconds):
  hours = seconds // 3600
  seconds = seconds % 3600
  minutes = seconds // 60
  seconds = seconds % 60
  return hours, minutes, seconds

def file_size(file_info):
  name, file_type, size = file_info
  return "{:.2f}".format(size / 1024)

def full_emails(people):
  result = []
  for email, name in people:
    result.append("{} <{}>".format(name, email))
  return result

def odd_numbers(n):
  return [x for x in range (1, n + 1) if x % 2 != 0]

def pig_latin(text):
  say = ""
  words = text.split()
  for index, word in enumerate(words):
    if index > 0:
      say += " "
    say += word[1:] + word[0] + "ay"
  return say

def octal_to_string(octal):
  result = ""
  value_letters = [(4, "r"), (2, "w"), (1, "x")]
  for digit in [int(n) for n in str(octal)]:
    for value, letter in value_letters:
      if digit >= value:
        result += letter
        digit -= value
      else:
        result += "-"
  return result

def group_list(groups, users):
  members = groups + ":"
  for index, user in enumerate(users):
    if index > 0:
      members += ","
    members += " " + user
  return members

def guest_list(guests):
  for guest in guests:
    name, age, job = guest
    print("{} is {} years old and works as {}".format(name, age, job))

x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))
print("are" in x)
print("Today" in x)
print(x[0])
print(x[3])
print(x[1:3])
print(x[:2])
print(x[2:])

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# append
fruits.append("Kiwi")
print(fruits)
# insert
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(1000, "Peach")
print(fruits)
# remove
fruits.remove("Melon")
print(fruits)
# pop
print(fruits.pop(3))
print(fruits)
fruits[2] = "Strawberry"
print(fruits)

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

# tuples
fullname = ('Grace', 'M', 'Hopper')
result = convert_seconds(5000)
print(type(result))
hours, minutes, seconds = result
print(hours, minutes, seconds)

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
  chars += len(animal)
print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index, person in enumerate(winners):
  print("{} - {}".format(index + 1, person))

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

multiples = []
for x in range(1, 11):
  multiples.append(x * 7)
print(multiples)
# list comprehension
multiples = [x * 7 for x in range (1, 11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)

z = [x for x in range (0, 101) if x % 3 == 0]
print(z)

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
for file in filenames:
  if file.endswith(".hpp"):
    newfilenames.append(file[:-4] + ".h")
  else:
    newfilenames.append(file)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])