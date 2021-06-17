#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
print("welcome to the tip calculator.")
total_bill=float(input("what was the total bill? $"))

percentage_number =int(input(f"what percentage tip would you like to give? 10, 12, 15? " ))
added_tip=percentage_number/100 +1

no_of_people=int(input("How many people to split the bill? "))

split_bill=(total_bill/no_of_people)*float(added_tip)

final_bill=(round(split_bill,2))
final_bill="{:.2f}".format(split_bill)
print(f"Each person should pay: ${final_bill}")


