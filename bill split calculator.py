
print("Welcome to the bill-split calculator!")

bill1 = float(input("What was the total bill? "))

percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))

people1 = float(input("How many people to split the bill? "))

z = bill1/people1 + (bill1*(percent/100))

#Total amount, round to two decimal places
y = round(z, 2)

print("Each person should pay: " + f"{y}")
