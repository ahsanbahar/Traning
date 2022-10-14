# def emp(name, ID, dept ):
#     return name, id, dept
# print (emp('a',1,'ban'))
# print (emp('b',3,'eng'))
# print (emp('c',4,'math'))
# print (emp('d',5,'eco'))
# print (type (id))

# def shop_total_sell(*args):
#     print (type(args))
#     sum = 0
#     for amount in args:
#         sum=sum+amount
#     return sum
# total_amount= shop_total_sell(23,34,43,45,56,67,68,89,90,55)

# print ('total sell amount:', total_amount )

# def add(**kwagrs):
#     print(type(kwagrs))
#     sum=0
#     for key in kwagrs:
#         sum=sum+kwagrs[key]
#     return sum
# total= add(a=2,b=5)
# print (total)

x=input("Enter a value for x : ")
y=input("Enter a value for y : ")

z=input("Options are (+-*/ or x for exit) : ")
while (z!=0):
  if (z=='+'):
    print(int(x)+int(y))
  elif(z=='-'):
    print(int(x)-int(y))
  elif(z=='*'):
    print(int(x)*int(y))
  elif(z=='/'):
    print(int(x)/int(y))
  elif (z=='x'):
    exit()
  z=input("Options are (+-*/ or x for exit) : ")
