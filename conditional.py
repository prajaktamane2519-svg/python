str1="this is a string"
print(str1)

str2 ="this is a string.\n we are creating it in python"
print(str2)
str3="this is a string.\t we are creating it in python"
print(str3)
str1 ="wakad"
str2="pune"
print(str1+str2) 
str ="apple"
print(str[-3:-1])
str1="i am studying"
print(str1.capitalize())
a="sagar"
print(a.replace("a", "o"))

b="i live in city "
print(str.find("i"))
print(b.find("live"))

print(b.count("i"))
name=input("enter your name : ")
print("length of your name is",len(name))
str6="hi ,$iam the $ symbol $99.99"
print(str6.count("$"))

age=21
if(age>=18):
    print("can vote and apply for license")

light="green"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
print("end of code")

light="pink"
if(light=="red"):
    print("stop")
elif(light=="green"):
    print("go")
elif(light=="yellow"):
    print("look")
else:
    print("light is broken")

marks=int(input("enter student mark : "))
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="c"
else:
    grade="D"
    print("grade of the student ->",grade)

number=int(input("enter the number : "))
if(number%2==0):
    print("Even number")
else:
    print("odd number")
number1=int(input("enter the number: "))
number2=int(input("enter the number: "))
if(number1>number2):
    print("largest number")
else:
    print("smallest number")

num=int(input("enter the number"))
if(num>0):
    print("positive number")
elif(num<0):
    print("negative number")
else:
    print("zero number")

age=int(input("enter the age: "))
if(age>=18):
    print("you can vote")
else:
    print("you can not vote")
year=int(input("enter the number: "))
if(year%4==0 and year %100!=0 or year%400==0):
    print("leaf year")
else:
    print("not a leaf year")
ch=input("enter a character: ")
if ch.lower() in "aeiou":
    print("vowel")
else:
    print("consonant")
num=int(input("enter a number:"))
if(num%5 == 0 and num%11 == 0):
    print("Divisible 5 and 11")
else:
    print("not divisible")
marks=int(input("enter the number: "))
if(marks>=35):
    print("pass")
else:
    print("fail")

a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
if(a>b and a>c):
    print("a is greatest")
elif( b>a and b>c):
    print("b is greatest")
else:
    print("c is gtreast")
marks=int(input("enter the marks : "))
if(marks>90):
    print("grade A")
elif(marks>78):
    print("grade B")
elif(marks>35):

    print("grade c")
else:
    print("Fail")

number=int(input("enter the number: "))
if(number>=100 and number<999):
    print("three digit number")
else:
    print("not three digit number")

a=int(input("enter the number: "))
if(a%3==0 and a%5==0):
    print("divisible by both")
else:
    print("not divisible by both")
ch=input("enter the character : ")
if(ch.isupper()):
    print("uppercase")
else :
    print("lowercase")
b=int(input("enter the number: "))
if(num>=1 and num<=100):
    print("number is in the rang")
else:
    print("number is out of the rang")
num=int(input("enter the number: "))
if(num<0):
    print(-num)
else:
    print(num)

a=int(input("enter the number : "))
b=int(input("enter the number : "))
c=int(input("enter the number : "))
if(a+b+c==180):
    print("valid triangle")
else:
    print("invalid triangle")
a=int(input("enter the number: "))
b=int(input("enter the number: "))
c=int(input("enter the number: "))
if(a==b==c):
    print("Equilater Triangle")
elif a==b or b==c or a==c:
    print("Isosceles Triangle")
else:
    print("scalene triangle")

age=int(input("enter the age: "))
if(age>18):
    print("person  Eligiblefor job")
else:
    print("not eligible")
experience=int(input("Enter year of experience : "))
if(experience>=5):
    print("bonus eligible")
else:
    print("not bonus")
amount=int(input("enter purchase amount : "))  
if (amount>=5000 ):
    print("20% Discount")
else:
    print("no discount")
balance=10000
amount=int(input("enter withdrawal amount : ")) 
if amount<=balance:
    print("transaction successful")
else:
    print("insufficient balance")

    