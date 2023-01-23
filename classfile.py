# class
class Person:
    # constructor
    # Note: The __init__() function is called automatically every time the class is being used to create a new object.

    # public attribute
    schoolName = 'XYZ School'  # class attribute
    # protected attribute

    # privet attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Normal Method
    def my_func(self):
        print(f"my name is {self.name} and age is {self.age}")
    # Access modifiers


# p object
p = Person("Imtiaz Khandoker", 28)
p.my_func()
