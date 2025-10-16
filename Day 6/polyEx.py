# class Bird:
#     def fly(self):
#         print('Bird can fly')

# class Airplane(Bird):
#     def fly(self):
#         print('Airplane fly')

# b=Bird()
# print('Bird Implement')
# b.fly()

# print('Airplane Implementation')
# a=Airplane
# a=fly()

# print('Using for loop')
# for obj in [Bird(),Airplane()]:
#     obj.fly()

#---------------------------------------------------------------
class Emp:
    def reg(self):
        self.id=int(input('Enter Id: '))
        self.name=input('Enter Name: ')

    def display(self):
        print("Name: ",self.name)
        print("Id: ",self.id)

class Dev(Emp):
    def reg(self):
        super().reg()
        self.domain=input('Enter Domain: ')

    def display(self):
        super().display()
        print('Domain: ',self.domain)

d1=Dev()
d1.reg()
d1.display()