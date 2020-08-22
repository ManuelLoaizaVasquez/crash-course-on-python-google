def format_address(address_string):
  strings = address_string.split()
  number = strings[0]
  address = ""
  for index, string in enumerate(strings):
    if index > 0:
      if index > 1:
        address += " "
      address += string
  return "house number {} on street named {}".format(number, address)

'''
def highlight_word(sentence, word):
  words = sentence.split()
  result = ""
  for index, token in enumerate(words):
    if index > 0:
      result += " "
    if token == word:
      result += token.upper()
    else:
      result += token
  return result
'''
def highlight_word(sentence, word):
  return sentence.replace(word, word.upper())

def combine_lists(list1, list2):
  result = list2
  for i in range(len(list1)):
    result.append(list1[len(list1) - 1 - i])
  return result

def squares(start, end):
  result = []
  for n in range(start, end + 1):
    result.append(n * n)
  return result

def car_listing(car_prices):
  result = ""
  for model, price in car_prices.items():
    result += "{} costs {} dollars".format(model, price) + "\n"
  return result

def combine_guests(guest1, guest2):
  result = {}
  for name, number in guest1.items():
    if name not in result:
      result[name] = number
  for name, number in guest2.items():
    if name not in result:
      result[name] = number
  return result

def count_letters(text):
  result = {}
  for letter in text:
    current = letter.lower()
    if 'a' <= current and current <= 'z':
      if current not in result:
        result[current] = 0
      result[current] += 1
  return result

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"
print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"
print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
print(combine_lists(Jamies_list, Drews_list))

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())