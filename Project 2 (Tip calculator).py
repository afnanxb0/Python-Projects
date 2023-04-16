print("Welcome to the tip calculator!!")


#float() = number with decimal
bill = float(input("What is the total bill? $"))


#int()= turning into integer
tip = int(input("What percentage tip would you like to give?"))


people = int(input("How many people would like to split?"))
bill_with_tip = tip/100 * bill + bill
bill_per_person = bill_with_tip / people


#round = show round number
final_amount = round(bill_per_person, 2)


#"{:.2f}".format = decimal formating
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")
