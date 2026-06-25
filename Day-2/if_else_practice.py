#Even or Odd 
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Greatest of Two Numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print(a, "is greater")
else:
    print(b, "is greater")

#Positive, Negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Voting Eligibility 
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

#Greatest of Three Numbers 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b:
    if a >= c:
        print(a, "is the greatest")
    else:
        print(c, "is the greatest")
else:
    if b >= c:
        print(b, "is the greatest")
    else:
        print(c, "is the greatest")

print("\n🎉 Day 2 Completed!")
