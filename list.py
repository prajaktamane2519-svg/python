my_list=[1,2,3]
print(my_list)
my_list2=[1,2,[2,4],True,[4.,5,8]]
print(my_list2)
print(type(my_list2))
my_list=[9,56,89]
print(my_list)
list=[10,20,30,40]
print(list[0])
print(list[1])
print(list[-1])
print(list[-2])
print(list[0:3])
print(list[1:5])
print(list[-3: ])
print(list[ :: ])
print(list[ :: 2])
my_list4=['apple','banana','cherry']
print(my_list4)
my_list4[1]='blueberry'
print(my_list4)
my_list4.append("mango")
print(my_list4)
my_list4.remove("cherry")
print(my_list4)
colour=["pink","red","white"]
colour.append("black")
print(colour)
colour1=["yellow","orage"]
colour.extend(colour1)
print(colour)
colour.remove("red")
print(colour)
fruits=["apple","orange"]
fruits.insert(1,"blueberry")
print(fruits)
fruits=["apple","banana","cherry","cherry","banana"]
index=fruits.index("cherry")
print(index)
index=fruits.index("banana",1)
print(index)
index=fruits.index("banana")
print(index)
fruits=["apple","banana","cherry","cherry","banana"]
fruits.reverse()
print(fruits)
fruits=["apple","banana","cherry","cherry","banana"]
fruits.sort()
print(fruits)
fruits.sort(key=len,reverse=True)
print(fruits)
numbers=[10,20,30,40]
popped=numbers.pop(2)
print(popped)
print(numbers)
last=numbers.pop()
print(last)
print(numbers)
copy_fruits=fruits.copy()
print(copy_fruits)
copy_fruits.append("mango")
print(copy_fruits)
print(fruits)

list1=[1,5,7,8]
list2=[2,4,9,78]
final_list=list1+list2
print(final_list)
for x in list2:
    list1.append(x)
print(list1)
list1.extend(list2)
print(list1)
square=[x**2 for x in range(1,6)]
print(square)
even_list=[x for x in range(1,10) if x%2==0]
print(even_list)
fruits=["apple","banana","cherry","cherry","banana"]
print(fruits)
uppercase_list=[1st.upper() for 1st in fruits]
print(uppercase_list)

