s="python"
print(s)
print(len(s))
print(s[0])
print(s[-1])
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.strip())
s="i love java"
print(s.replace("java" ,"python"))
s="banana"
print(s.count("a"))
print(s.find("a"))
print(s.startswith("b"))
print(s.endswith("a"))
print("a"in s)
print(s.isalpha())
s="786"
print(s.isdigit())
s="python123"
print(s.isalnum())
print(s[::-1])
for ch in s:
    print(ch)
s="python"
count=0
for ch in s:
    if ch in "aeiou":
        count+=1
print(count)
s="python"
count=0
for ch in s:
    if ch.isalpha()and ch not in "aeiou":
        count+=1
print(count)
s="i  love python "
print(s.count(" "))
w=s.split()
print(len(w))
print(s.replace(" ",""))
s=" i love python"
print(s.replace(" ","_"))
s="madam"
if s== s[::-1]:
    print("s is palidrom")
else:
    print("s is not")
s1="python"
s2="python"
if s1==s2:
    print("equal")
else:
    print("not equqal")
s="python is easy"
print(s.title())
