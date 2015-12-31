#Investing Game!!!
#This is my first project on my own
#Try for a high score!
#Mine is $34,194.04
import random

#Functions
#Function to determine real estate amount:
def real_estate(amount):
    amount = float(amount) + float(amount) * random.uniform (-.3, .3)
    return amount
#Function to determine stock amount:
def stocks(amount):
    amount = float(amount) + float(amount) * random.uniform (-.99, .99)
    return amount
#Function to determine bond amount:
def bonds(amount):
    amount = float(amount) + float(amount) * random.uniform (-.1, .1)
    return amount
#The next two functions are used to find remaining in bank account:
def bank_account(amount):
    amount = float(amount) + float(amount) * random.uniform (.0001, .02)
    return amount
def end():
    amount = float(tot_amount) - (float(one_real) + float(one_stock) + float(one_bond))
    return amount

#Starting amount
tot_amount = 10000
#Starting Instructions
print ("Welcome to Investing Game.")
start = input("Press Enter to Start.")
print ("Hello Chief")
print ("You just inherited $10,000 dollars and you arn't satisfied.")
print ("You have 5 years to grow your funds to the largest amount possible")
print ("You can invest in real estate, stocks, bonds or just leave the money in your bank account")
print ("Stocks are the riskiest but have the highest returns.")
print ("The rest from risky to not risky are as follows: ")
print ("Real Estate, Bonds and leaving your money in your bank account")
i = 0
#The main loop of the game. Set to go through 5 times which equals 5 years.
while (i<5):
    next = input("Press Enter to continue.")
    i = i + 1
    print ("Year " + str(i))
    #tot_amount is changed each year depending on if you made money or lost money
    print ("You have $" + str(tot_amount) + (" dollars ready to invest."))
    #These loops make sure that input is valid and under tot_amount:
    while True:
        try:
            one_real = float(input ("How much do you want to invest into real estate?"))
        except ValueError:
            print("Sorry, please try again.")
            continue
        if one_real > tot_amount:
            print("You only have " + str(tot_amount) + " to invest. Try again.")
            continue
        else:
            break
    while True:
        try:
            one_stock = float(input ("How much do you want to invest into stocks?"))
        except ValueError:
            print("Sorry, please try again.")
            continue
        if (one_real + one_stock) > tot_amount:
            print("You only have " + str(tot_amount - one_real) + " to invest. Try again.")
            continue
        else:
            break    
    while True:
        try:
            one_bond = float(input ("How much do you want to invest into bonds?"))
        except ValueError:
            print("Sorry, please try again.")
            continue
        if (one_real + one_stock + one_bond) > tot_amount:
            print("You only have " + str(tot_amount - (one_real + one_stock)) + " to invest. Try again.")
            continue
        else:
            break 
    
    #All extra money will put into bank account.
    print ("The rest will be left in your bank account.")

    next = input ("Press Enter.")
    #These result values were added to insure that the random number was only applied once in the following 5 prints.
    result_one_real = real_estate(one_real)
    result_one_stock = stocks(one_stock)
    result_one_bond = bonds(one_bond)
    result_one_bank = bank_account(end())
    print ("Your new total is $" + str( round(float(result_one_real) + float(result_one_stock) + float(result_one_bond) + float(result_one_bank),2)))
    print ("You made $" + str( round(float(result_one_real) - float(one_real),2)) + " in real estate.")
    print ("You made $" + str( round(float(result_one_stock) - float(one_stock),2)) + " in stocks.")
    print ("You made $" + str( round(float(result_one_bond) - float(one_bond),2)) + " in bonds.")
    print ("You made $" + str( round(float(result_one_bank) - end(),2)) + " in your bank account.")
    #Here is how tot_amount is calculated
    tot_amount = round(float(result_one_real) + float(result_one_stock) + float(result_one_bond) + float(result_one_bank),2)
print ("This is your total after five years of investment: $" + str(tot_amount))
#The End

