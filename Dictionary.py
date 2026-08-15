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