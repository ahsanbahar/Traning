from cgi import print_arguments

'''
class class5:
    a=4
    b=9
bahar = class5()
bahar1=class5()

print (bahar.a,bahar.b)
print(bahar1.a)
'''
class cal:
    def add(self,num1,num2):
        return num1+num2
    def sub(self,num1,num2):
        return num1-num2
    def mult(self, num1,num2):
        return num1*num2
    def div(self,num1,num2):
        return num1/num2            
bahar = cal()
print(bahar.add(5,5),bahar.sub(10,5),bahar.mult(3,4),bahar.div(10,2))

