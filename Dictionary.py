student={"name":"ask","age":4,"grade":"A"}
print(student)
print(student["name"])
print(student.get("age"))
student["city"]="new york"
student["age"]=8
print(student)
student.pop("grade")
del student["city"]
student={"name":"era","age":7,"city":"pune"}
print(student)
print(student["name"])
print(student["age"])
student["city"]="karad"
student["age"]=9
print(student)

if "name" in student:
    print("Name exist")
print(len(student))
a={}
a["name"]="oi"
a["age"]=7
print(student.keys())
print(student.values())
print(student.get("age"))
print(student.get("city"))
(student.pop("age"))
print(student)
student.clear()
print(student)
student={"name":"Dsk","age":8,"marks":67}
new_student=student.copy()
print(new_student)
student={"name":"pdk","age":9}
student.update({"city":"pune"})
print(student)
for key in student:
    print(key)
for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)
marks={"A":70,"B":80,"c":30,"D":30}
count=0
for value in marks.values():
    if value>50:
        count+=1
print(count)
total=0
for value in marks.values():
    total+=value
print(total)
marks={"A":70,"B":60,"c":50}
print(max(marks.values()))
print(min(marks.values()))
for key,value in marks.items():
    if value%2==0:
        print(key)
student={"amit":60,"rahul":78,"priya":67}
for name,marks in student.items():
    if marks>75:
        print(name)




