for i in range(1,100):
    print(i)

ting=0
for i in range(1,100):
    sum=ting+i
    print(sum)
print(sum)

#print odd number
for i in range(1,100,2):
    print(i)

#print even number
for i in range(2,101,2):
    print(i)

#sum of even numbers
sum=0
for i in range(2,100,2):
    sum=sum+i
    print(sum)

#sum of odd numbers
sum=0
for i in range(1,100,2):
    sum=sum+i
    print(sum)

#print star(*) in a pattern

for i in range(1,4):
    for j in range(1,i+1):
        print("*", end=" ")
    print()

# While loop
count=5
while count>0:
    print(count)
    count=count-1

