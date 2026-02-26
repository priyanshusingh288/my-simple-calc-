principle=0
rate=0
time=0

while principle<=0:
    principle=float(input("enter the principle for the compound interest"))
    if principle<=0:
        print("principle cannot be zero or cannot be negative")


while rate<=0:
    rate=float(input("enter the rate for the compound interest"))
    if rate<=0:
        print("rate cannot be zero or cannot be negative")

while time<=0:
    time=float(input("enter the time for the compound interest"))
    if time<=0:
        print("time cannot be zero or cannot be negative")


total=principle*pow((1+rate/100),time)  
print(f"the compound intrest would be {total}")
