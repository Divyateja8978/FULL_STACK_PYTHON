#list operators
list1 = [10, 20, 30]
list2 = [40, 50, 60]

print(list1 + list2)
print(list1 * 2)
print(20 in list1)
print(100 not in list1)
print(list1 == list2)

#list builtin methods
list1 = [30, 10, 20, 10]

list1.append(40)
print(list1)
list1.insert(1, 15)
print(list1)
list1.remove(10)
print(list1)
print(list1.pop())
print(list1)
print(list1.index(20))
print(list1.count(10))
list1.sort()
print(list1)
list1.reverse()
print(list1)
list1.clear()
print(list1)

#tuple operators
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
print(tuple1 + tuple2)
print(tuple1 * 2)
print(20 in tuple1)
print(100 not in tuple1)
print(tuple1 == tuple2)

#tuple builtin methods
t = (10, 20, 30, 20, 40, 20)
print(t.count(20))
print(t.index(30))
