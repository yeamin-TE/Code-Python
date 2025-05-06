marks = float(input("Enter your marks:"))

if marks >= 80:
    gpa= "5.00"
elif marks >=70:
    gpa= "3.5"
elif marks >= 60:
    gpa = "3.00"
elif marks >=50:
    gpa = "2.5"
elif marks >=40:
    gpa = "2.00"
else:
    gpa= "Failed"
    
print("gpa=",gpa)