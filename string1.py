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