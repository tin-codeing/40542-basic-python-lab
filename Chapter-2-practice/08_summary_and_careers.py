meal = float(input("Enter how much the meal?: "))
tip = float(input("how much the tip?: "))
member = int(input("and how many member did you have?: "))

tip_in = meal * (tip / 100)
All_total = meal + tip_in
havetopay_person = All_total / member

print(f"Each person pays: {havetopay_person:.2f}")