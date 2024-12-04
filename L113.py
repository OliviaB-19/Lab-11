##The authors are Olivia and Lily

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+ str(self.age) + ")"

p1 = Person("John", 36)

print(p1)

##I think it will return John and 36 is the same line but I don't know how it will be formatted

##I was right, I think it is different because with the return, it stays in the same line and separates the second value form the first with parentheses
