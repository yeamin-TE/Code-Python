Secretcode = 7
guess = int(input("Enter a number from 1-10 :"))

if 1<= guess <=10:
    if guess== Secretcode:
        print("Congrats, Your guess is correct")
    else:
        print("Sorry, Your guess is wrong, correct code was",Secretcode)

else:
    print("Your guess must be from 1-10")        
    