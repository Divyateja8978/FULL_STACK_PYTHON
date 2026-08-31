#if:
age = 20
if age >= 18:
    print("Eligible to vote")
#elif:
age = 16
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
#elif else
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")
#Nested if
age = 20
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not a citizen")
else:
    print("Under 18")