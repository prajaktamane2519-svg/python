def greetings():
    print("welcome to the python course by ri")
greetings()
def add2numbers(a,b):
    result=a+b
    print("the sum is:",result)
add2numbers(7,8)
def add2num(a,b):
    return a+b
    return a-b
sum2num=add2num(10,1)
print(sum2num)
def greeting(name):
    print("HEllo",name, "!")
greeting("akash")

def intro(course_name,project_name):
    print("welcome to",course_name,"course by",project_name)
intro("pyrhon","calucator")
def clg(name="sgn"):
    print("welcome to",name)
clg()
clg("pgm")
def divide(a,b):
    return a/b
result=divide(a=10,b=20)
print(result)

def add(*args):
    return sum(args)
op=add(1,2,6,7)
print(op)


def print_details(**Kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
    print_details(name="adhav",age=34,city="pune")

        