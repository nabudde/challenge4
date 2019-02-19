year=input("Enter your year of birth")
x = int(year)
age = 2019 - x
if age < 18:
    print("minor")
elif age >=18 and age<=36:
    print("youth")
else:
    print("elder")
   