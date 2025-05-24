marks= int(input("Enter your marks:"))

if marks>=80 and marks<=100:
    print("Grade is: A+")
elif marks>=70 and marks<=79:
    print("Grade is: A")
elif marks>=60 and marks<=59:
    print("Grade is: A-")
elif marks>=50 and marks<=59:
    print("Grade is: B")
elif marks>=33 and marks<=49:
    print("Grade is: B-")
elif marks>=0 and marks<=32:
    print("Failed")   
else:
    print("Enter your marks between 1-100 to calculate your grade")