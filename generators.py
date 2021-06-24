class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2

        if self.num >5:
            raise StopIteration
        return num

z=InfIter()
for x in z:
    print(x)


def reas(lst):
    lst=[1,2]

def app(lst):
    lst.append(4)

x = 10
def function1():
  y = 7
  
  print("x in function1=", x)
  print("y in function1=", y)
  
  

function1()
print(x)

class Person:
  def __init__(self):
    self.name = "David"
    self.age = 32

  def display_data(self):
    print(self.name)
    print(self.age)

person = Person()
person.display_data()



def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        print("fib numbers")
        yield x

def square(nums):
    for num in nums:
        print("sqaure")
        yield num**2

print(sum(square(fibonacci_numbers(10))))


