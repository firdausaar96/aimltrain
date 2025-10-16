class Emp:
    def display(self):
        print("Display of Employee class")

obj=Emp()
obj.display()

#-----------------------------------------------------------------
#Second Example

class Emp:
    def reg(self,eid,ename):
        self.eid=eid
        self.ename=ename

    def display(self):
        print("Employee Details as follow: ")
        print("Employee ID: ",self.eid)
        print("employee Name: ",self.ename)

e1=Emp()
e2=Emp()
e3=Emp()
e1.reg(1,'Sam')
e2.reg(2,'Neha')
e3.reg(3,'Jai')

print("First Employee details: \n")
e1.display()
print("\nSecond Employee details: \n")
e2.display()
print("\nThird Employee details: \n")
e3.display()