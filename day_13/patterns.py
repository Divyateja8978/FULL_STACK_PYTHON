#square pattern
n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# Right angle
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    
#inverted triangle
n = 5
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    
#Number triangle
n = 5
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
    
#same unmber
n = 5

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
    
#increasing number
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num = num + 1
    print()