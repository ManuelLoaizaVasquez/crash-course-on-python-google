def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result

x = {}
print(type(x))

def email_list(domains):
  emails = []
  for domain, users in domains.items():
    for user in users:
      emails.append(user + "@" + domain)
  return emails

def groups_per_user(group_dictionary):
  user_groups = {}
  for group, users in group_dictionary.items():
    for user in users:
      if user not in user_groups:
        user_groups[user] = []
      user_groups[user].append(group)
  return user_groups

def add_prices(basket):
  total = 0
  for value in basket.values():
    total += value
  return round(total, 2)

file_counts = {"jpg" : 10, "txt" : 14, "csv" : 2, "py" : 23}
print(file_counts)
print(file_counts["txt"])
print("jpg" in file_counts)
print("html" in file_counts)
file_counts["cfg"] = 8
print(file_counts)
file_counts["csv"] = 17
print(file_counts)
del file_counts["cfg"]
print(file_counts)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
print("Chapter 5" in toc)# Is there a Chapter 5?

for extension in file_counts:
  print(extension)

for extension, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, extension))

print(file_counts.keys())
print(file_counts.values())

for value in file_counts.values():
  print(value)

cool_beasts = {"octopuses" : "tentacles", "dolphins" : "fins", "rhinos" : "horns"}
for animal, extra in cool_beasts.items():
  print("{} have {}".format(animal, extra))

print(count_letters("aaaaa"))
print(count_letters("tenant"))
print(count_letters("a long string with a lot of letters"))

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for category, colors in wardrobe.items():
  for color in colors:
    print("{} {}".format(color, category))

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

print(groups_per_user({"local": ["admin", "userA"], "public":  ["admin", "userB"], "administrator": ["admin"] }))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,  "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}
print(add_prices(groceries)) # Should print 28.44