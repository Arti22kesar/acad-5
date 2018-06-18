#Ques1.

a=int(input("enter the year"))

if(a%4 == 0):
    print("The year is leap year")
    print(a)
else:
    print("The year is not leap year")


#Ques2.

length=input("enter the length")
breadth=input("enter the breadth")
if(length==breadth):
    print("square")
else:
    print("rectangle")


#Ques3.

a= int(input("enter the age"))
b= int(input("enter the age"))
c= int(input("enter the age"))
if(a>b):
    if(a>c):
     print("a is greater")
     print(a)
elif (b>c and b>a):
    print("b is greater")
    print(b)
else:
    print("c is greater")

if(a<b):
    if(a<c):
        print("a is smaller")
        print(a)
elif (b<c and b<a)   :
    print("b is smaller")
    print(a)
else:
    print("c is smaller")


#Ques4.

a=int(input("enter your points"))
if(a>=1 and a<=50):
    print("sorry!No prize this time")
    if(a>50 and a<=150):
        print("congratulation! you won a wooden dog ")
elif(a>150 and a==180):
        print("congratulation! you won a book")
elif(a>180 and a<=200) :
        print("congratulation! you won chocolates")
else:
    print ("sorry no prize")

#Ques5.

a=int(input("enter the quantity of the goods"))
e=a*100
if(e>1000):
    b=e*0.1
    c=e-b
    print("Discount given is")
    print(b)
    print("cost after discount is")
    print (c)
else:
 print("sorry no discount given")






