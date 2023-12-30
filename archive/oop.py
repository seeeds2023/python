class Person:
  def __init__(self, name, age, height):
    print(f'__init__ called with name: {name}, age: {age}, height: {height}')
    self.name = name
    self.age = age
    self.height = height

  def find_classroom(self, teacher_name):
    print(f'printing object attributes, name: {self.name}, age: {self.age}')
    if teacher_name == "Megha":
      print(f'class room is 104 for student {self.name}')
    else:
      print('class room is 208')

  def update_height(self, new_height):
    self.height = new_height

john = Person("John", 36, 175)
peter = Person("Peter", 43, 180)

print(f'Johns height: {john.height}')
print(f'Peter age: {peter.age}')

peter.update_height(160)
print(f'peter height: {peter.height}')
peter.age = 35
peter.height = 177
peter.name = 'something'
print(f'peter age: {peter.age}')
print(f'peter height: {peter.height}')
print(f'peter name: {peter.name}')


