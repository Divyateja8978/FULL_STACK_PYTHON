import re

text = "My phone number is 9876543210"

pattern = r"\d+"

result = re.findall(pattern, text)

print(result)
#simple email validation example
import re

email = input("Enter email: ")

pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+$"

if re.match(pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")
