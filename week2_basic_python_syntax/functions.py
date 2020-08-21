def greeting(name, department):
  print("Welcome, " + name)
  print("You are part of " + department)

def print_seconds(hours, minutes, seconds):
  total_minutes = minutes + 60 * hours
  total_seconds  = seconds + 60 * total_minutes
  print(total_seconds)

def area_triangle(base, height):
  return base * height / 2

def get_seconds(hours, minutes, seconds):
  total_minutes = minutes + 60 * hours
  total_seconds = seconds + 60 * total_minutes
  return total_seconds

def convert_seconds(seconds):
  hours = seconds // 3600
  remaining_seconds = seconds % 3600
  minutes = remaining_seconds // 60
  remaining_seconds = remaining_seconds % 60
  return hours, minutes, remaining_seconds

def month_days(month, days):
  print(month + " has " + str(days) + " days.")

def rectangle_area(base, height):
  area = base * height
  print("The area is " + str(area))

def convert_distance(miles):
  km = miles * 1.6
  return km

def order_numbers(number1, number2):
  if number2 > number1:
    return number1, number2
  else:
    return number2, number1

def lucky_number(name):
  number = len(name) * 9
  message = "Hello " + name + ". Your lucky number is " + str(number)
  return message

greeting("Manuel", "Mathematics")

print_seconds(1, 2, 3)

area_a = area_triangle(5, 4)
area_b = area_triangle(7, 3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum))

amount_a = get_seconds(2, 30, 0)
amount_b = get_seconds(0, 45, 15)
result = amount_a + amount_b
print(result)

hours, minutes, seconds = convert_seconds(5000)

month_days("June", 30)
month_days("July", 31)

rectangle_area(5, 6)

my_trip_miles = 55
my_trip_km = convert_distance(my_trip_miles)
print("The distance in kilometers is " + str(my_trip_km))
print("The round-trip in kilometers is " + str(2 * my_trip_km))

smaller, bigger = order_numbers(100, 99)
print(smaller, bigger)

print(lucky_number("Kay"))
print(lucky_number("Cameron"))