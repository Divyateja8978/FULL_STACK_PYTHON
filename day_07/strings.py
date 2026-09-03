#string operations
s = "Python Programming"
print("Length:", len(s))
print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("First character:", s[0])
print("Last character:", s[-1])
print("Slice:", s[0:6])
print("Replace:", s.replace("Python", "Java"))
print("Count:", s.count("m"))

#builtin methods
s = "python programming"

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.replace("python", "java"))
print(s.count("p"))
print(s.find("programming"))
print(s.startswith("python"))
print(s.endswith("ing"))
print(s.split())