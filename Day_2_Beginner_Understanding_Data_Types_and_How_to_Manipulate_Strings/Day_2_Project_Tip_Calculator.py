print("Welcome to the bill calculator.")
bill = float(input("What was the total bill : $"))
tip = int(input("What percentage of tip do you wanna give : 10, 12, 15 : "))
people = int(input("How many people to split the bill : "))
tip = bill * (tip / 100)
total_bill = tip + bill
final_bill = round(total_bill/people, 2)
print(f"Each person should pay ${final_bill}")