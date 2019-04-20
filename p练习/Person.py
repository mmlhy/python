class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def great(self):
        print("Hellow,my name is ",self.name + ". I am 11 years old")
tom = Person('tom',12)
tom.great()

jerry = Person('jerry',12)
jerry.great()

