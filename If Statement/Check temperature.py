Temperature = float(input("Enter today's temprature(celcius):"))

if Temperature<0:
    print("Weather is very cold")
elif 0<= Temperature <=15:
    print("Weather is cold")
elif 15< Temperature <=30:
    print("Weather is moderate")
else:
    print("Weather is hot")