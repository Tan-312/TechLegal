class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def displayData(self):
    print('In parent class displayData method')
    print(self.name)
    print(self.age)

class Employee(Person):
  def __init__(self, name, age, id):
    # calling constructor of super class
    super().__init__(name, age)
    self.empId = id

  def displayData(self):
    print('In child class displayData method',self.name,self.age)
    #calling super class method
    super().displayData()
    print(self.empId)

#Employee class object
emp = Employee('John', 40, 'E005')
emp.displayData()

class Person:
  '''Class Person displaying person information'''
  #class variable
  person_total = 0
  def __init__(self, name, age):
    print('init called')
    self.name = name
    self.age = age
    Person.person_total +=1
    print('pt',self.person_total)

  def display(self):
    print(self.name)
    print(self.age)

# printing doc string
print(Person.__doc__)
# creating class instances
person1 = Person('John', 40)
person1.display()
person2 = Person('Lila', 32)
person2.display()
print('Count- ', Person.person_total)



Overloading ‘+’ operator to work with custom objects

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  #overriding magic method
  def __add__(self, other):
    return self.x + other.x, self.y + other.y

p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1+p2)

print("done")