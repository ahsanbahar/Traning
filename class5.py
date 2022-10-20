class FirstClass:
    p_d = 5
    b = 8
belal = FirstClass()
student2 = FirstClass()

print(belal.b)

class EmpName:
    f_name='Md.'
    l_name='Hasanuzzaman'

emp=EmpName()

print(EmpName.f_name,EmpName.l_name)

class MyCal:
    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def multiplication(self,a,b):
        return a*b

    def division(self,a,b):
        return a/b


x=int(input("Enter a value for x : "))
y=int(input("Enter a value for y : "))

Calc1=MyCal()

print (Calc1.add(x,y))
print (Calc1.sub(x,y))
print (Calc1.multiplication(x,y))
print (Calc1.division(x,y))