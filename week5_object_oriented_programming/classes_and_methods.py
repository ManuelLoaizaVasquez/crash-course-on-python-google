class Piglet:
  """ Represents a piglet that can say their name."""
  name = "piglet"
  years = 0
  def speak(self):
    """ Outputs a message including the name of the piglet."""
    print("Oink! I'm {}! Oink!".format(self.name))
  def pig_years(self):
    """ Converts the current age to equivalent pig years. """
    return self.years * 18

hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()

petunia = Piglet()
petunia.name = "Petunia"
petunia.speak()

piggy = Piglet()
piggy.years = 2
print(piggy.pig_years())

class Dog:
  years = 0
  def dog_years(self):
    return self.years * 7

fido = Dog()
fido.years = 3
print(fido.dog_years())

class Apple:
  def __init__(self, color, flavor):
    self.color = color
    self.flavor = flavor
  def __str__(self):
    return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold.color)
print(jonagold)
help(Apple)

# docstrings
def to_seconds(hours, minutes, seconds):
  """ Returns the amount of seconds in the given hours, minutes and seconds."""
  return hours * 3600 + minutes * 60 + seconds

help(to_seconds)
help(Piglet)

class Elevator:
  def __init__(self, bottom, top, current):
    """Initializes the Elevator instance."""
    self.bottom = bottom
    self.top = top
    self.current = current
    pass
  def up(self):
    """Makes the elevator go up one floor."""
    self.current = min(self.top, self.current + 1)
    pass
  def down(self):
    """Makes the elevator go down one floor."""
    self.current = max(self.bottom, self.current - 1)
    pass
  def go_to(self, floor):
    """Makes the elevator go to the specific floor."""
    self.current = floor
    pass
  def __str__(self):
    return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
elevator.up() 
print(elevator.current) #should output 1
elevator.down() 
print(elevator.current) #should output 0
elevator.go_to(10) 
print(elevator.current) #should output 10
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
elevator.go_to(5)
print(elevator)