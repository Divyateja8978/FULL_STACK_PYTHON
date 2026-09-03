#set operators
s1 = {10, 20, 30}
s2 = {30, 40, 50}
print(s1 | s2)   # Union
print(s1 & s2)   # Intersection
print(s1 - s2)   # Difference
print(s1 ^ s2)   # Symmetric Difference
print(s1 == s2)  # Equal
print(20 in s1)  # Membership

#set builtin methods
s = {10, 20, 30}
s.add(40)
print(s)
s.update([50, 60])
print(s)
s.remove(20)
print(s)
s.discard(100)
print(s)
print(s.pop())
print(s)
s.clear()
print(s)

#dictinoary operators
d1 = {"a": 10, "b": 20}
d2 = {"c": 30, "d": 40}
print(d1 == d2)
print(d1 != d2)
print("a" in d1)
print("x" not in d1)
#builtin methods
d = {"name": "Divya", "age": 22, "city": "Hyderabad"}

print(d.keys())
print(d.values())
print(d.items())
print(d.get("name"))

d.update({"age": 23})
print(d)

d.pop("city")
print(d)

d.clear()
print(d)