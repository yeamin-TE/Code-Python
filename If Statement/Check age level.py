Age = int(input("Enter your age:"))

if 0< Age <=12:
    print("You are a child")
elif 13<= Age <=19:
    print("You are a teenager")
elif Age>19:
    print("You are an adult")
else:
    print("You have entered a wrong number")