# Conditional Statement

# IF statement
ph_balance = 3
bank_balance = 100

print(ph_balance,bank_balance)

if ph_balance < 5:
    ph_balance += 10
    bank_balance -= 10

print(ph_balance,bank_balance)

# IF,ELIF,ELSE statement

n = 59
if n % 2 == 0:
    print("Number "+str(n)+"is "+"Even")
else:
    print("Number "+str(n)+"is "+"odd")

print(n)

season = "spring"

if season == "spring":
    print("Spring")
elif season == "summer":
    print("Summer is worth")
elif season == "autumn":
    print("Autumn is beautiful")
else:
    print("Uncategorized season")

# Quiz
#Practice: Which Prize
#Write an if statement that lets a competitor know which of these prizes they won based on the number of points they scored, which is stored in the integer variable points.

#Points	Prize
#1 - 50	wooden rabbit
#51 - 150	no prize
#151 - 180	wafer-thin mint
#181 - 200	penguin


