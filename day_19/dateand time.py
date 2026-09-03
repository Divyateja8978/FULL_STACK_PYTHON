#date and time 
import datetime

today = datetime.date.today()
now = datetime.datetime.now()

print("Today's Date:", today)
print("Current Date and Time:", now)
print("Current Time:", now.strftime("%H:%M:%S"))

#create and write to afile
file = open("data.txt", "w")

file.write("Hello Python\n")
file.write("This is a file operation program.")

file.close()

print("Data written successfully")

#Read a File
file = open("data.txt", "r")

data = file.read()

print(data)

file.close()

#Append Data to a File
file = open("data.txt", "a")

file.write("\nWelcome to Python")

file.close()

print("Data appended successfully")
#Read Line by Line
file = open("data.txt", "r")

for line in file:
    print(line)

file.close()
#count number of words
file = open("data.txt", "r")

data = file.read()
words = data.split()

print("Number of words:", len(words))

file.close()
