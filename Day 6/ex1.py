# class player:
#     def __init__(self):
#         print('Welcome to Player Class')

#     def reg(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f"Id: {self.id} - Name: {self.name} - Team: {self.team} ")


# #object creation
# p1=player()
# p2=player()
# p3=player()

# p1.reg(1, 'MSD','India')
# p2.reg(2, 'R.Khan','Afghanistan')
# p3.reg(3, 'Ali','England')

# p1.display()
# p2.display()
# p3.display()

#----------------------------------------------------------------------------
#Parameterised Constructor

# class Player:
#     def __init__(self,id,name,team):
#         self.id=id
#         self.name=name
#         self.team=team

#     def display(self):
#         print(f"Id: {self.id} - Name: {self.name} - Team: {self.team} ")


# #object creation
# p1=Player(1, 'MSD','India')
# p2=Player(2, 'Joe','Afghanistan')
# p3=Player(3, 'Ali','England')

# p1.display()
# p2.display()
# p3.display()

#----------------------------------------------------------------------------
#Parameterised Constructor

class Player:
    def __init__(self,id,name,team):
        self.id=id
        self.name=name
        self.team=team

    def display(self):
        print(f"Id: {self.id} - Name: {self.name} - Team: {self.team} ")


#object creation
p1=Player(1, 'MSD','India')
p2=Player(2, 'Joe','Afghanistan')
p3=Player(3, 'Ali','England')

p1.display()
p2.display()
p3.display()
