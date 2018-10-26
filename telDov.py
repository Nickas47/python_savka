class Person:
    def __init__(self):
        self.name = None
        self.age = None
        
    def input(self):
        self.name = input("Введіть ім'я:")
        self.age = input("Введіть вік:")
        
    def print(self):
        print(self.name, self.age)
        
class Friend(Person):
    def __init__(self):
        super(Person,self).__init__()

    def input(self):
        Person.input(self)
        self.tel = input("Введіть номер телефону:")
        
    def __str__(self):
        return f'{self.name} {self.age} {self.tel}'
class Telefon(Person,Friend):

    def __init__(self):
        super().__init__()

    def number(self):
        a = raw_input('Введіть номер телефону')
        reader = open("TelDov.txt", "w+")
        name = None
        for row in reader:
            if a == row[2]:
                name = row[0], row[1]
                if name:
                    print(name)
                else:
                    print ('Phone not found')
       

x = Person()
y = Friend()
y.input()
print(y)
