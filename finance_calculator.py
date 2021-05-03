import math

calculator = input("Choose either 'investment' or 'Bond' to proceed:/n" + "investment-to calculate the amount of "
                                                                          "interest you'll earn on interest/n" +
                   "Bond-To calculate the amount you'll have to pay on a home loan")  # user must enter their

if calculator == "investment" or "INVESTMENT":  # if user selects investment
    deposit = int(input("Enter the amount of money you are depositing"))  # prompt user to enter deposit

    interest_rate = int(input("Enter the interest rate(only the amount,not percentage)"))  # prompt user to enter
    # interest-rate

    years = int(input("Enter the number of years you're willing to invest for"))  # prompt user to enter number of years
    interest = int(input("Would you like compound or simple interest"))  # ask user to choose between compound or
    # simple interest

if interest == "simple":  # if user selects simple interest
    final_amount = deposit(1 + interest_rate * years)  # calculate the amount the user will receive
elif interest == "compound":  # if user selects compound
    final_amount = deposit * math.pow((1 + interest_rate), years)  # calculate amount user will receive using compound
    # interest rate
    print("The amount of money you'll have after the investment is", final_amount)  # print the amount

if calculator == "bond" or "BOND":  # if user selects bond
    value = int(input("What is the present value of the house"))  # prompt user to enter value of the house
    interest_rate = int(input("Enter the interest rate(only the amount,not percentage)"))  # prompt user to enter
    # interest rate
    months = int(input("Enter the number of months you plan to re-pay the bond"))  # enter number of months
    amount = (interest_rate * value) / math.pow(1 - (1 + interest_rate), -months)  # calculate the amount that needs to
    # be paid monthly
    print("The amount of money due for the bond payment every month is:" + amount)  # print the amount
