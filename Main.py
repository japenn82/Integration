##Joshua Penn
##COP 1500 - Integration Project
##Application to assist with budgeting monthly finances

print("Welcome to Josh's Python Integration Project.")
name = input("May I have your name, please?")
print("Hi,", name.capitalize()+"!")
print("The purpose of this program is to assist you in budgeting your personal finances. Does that interest you?")
response = input("Please respond to the question with YES or NO :\n")

##I found out how to use 'if statement with strings' from the following stackoverflow website:
##https://stackoverflow.com/questions/6762959/if-statement-for-strings-in-python
if response.lower() in ['yes']:
    print("Awesome! I'm glad you're interested!\n")
elif response.lower() in ['no']:
    print("That's too bad. Perhaps another time then. This program will now exit.")
    exit()
elif response.lower():
    print("Please try again.")
    response = input("Enter YES or NO :\n")
    if response.lower() in ['yes']:
        print("Great!")
    else:
        print("Thanks for stopping by. Try again later.")
        exit()

##This section collects data from user, assigning it to variables.
print("Please note: For all entries, please enter whole dollar amounts only--NO DECIMALS--and do not use commas.")
print("If any entry doesn't apply to you, just enter 0.\n")
print("First, you'll need to input you monthly income.\n")
income = int(input("How much do you earn each month? : "))
bonus = int(input("If you earn a yearly bonus, how much is it?"))
income += bonus/12
rent: int = int(input("\nNext, please enter your monthly rent expense amount: "))
if rent <= 500:
    print("\nWow! Great job on finding inexpensive rent!!")
if rent/income > .30:
    print("\nFYI: Your rent payment is greater than 30% of your gross monthly income. This is something that lenders take into consideration when applying for credit.")
car = int(input("\nCar payment amount: "))
if car == 0:
    print("\n   ~~~~Awesome!!~~~~ :-)")
print("\nFor insurance, please combine all insurance costs--health and auto, for example.")
insurance = int(input("How much are your monthly insurance expenses?: "))
gas = int(input("\nNow, approximate how much you spend on fuel for your car each month: "))
food = int(input("\nUp next, food. How much do you spend on food each month?: "))
cell = int(input("\nWhat about cell phone/service each month?: "))

##Now the provided data will be used to calculate expenses
print("\nGood job! Now, let's take a look at what you entered.")
print("\nYour average monthly income (including your annual bonus) is $", format(income,".2f"))
total_expenses = (rent + car + insurance + gas + food + cell)
print("Your total monthly expenses are $", total_expenses)
proceed = input("\nPress the ENTER key to continue...")

##Calculate and display monthly net income
print("\nNext, we'll calculate your net income. Net income is the difference between your income and expenses.")
print("Another way to look at it, is that it's how much money you have left after paying your expenses.")
net_income = (income - total_expenses)
print("Your average monthly net income is $", format(net_income, ".2f"))
print("\nNow that you know your net income, you have an idea about how much you money you have available each month.")
print("Let's take it a bit further though and see what your average available net income is each week,")
print("as that will make it easier for you to budget successfully.\n")
proceed = input("\nPress the ENTER key to continue...")

##Calculate and display weekly net income
weekly_net_income = (net_income * 12 / 52)
print("\nTo do this calculation, we take your monthly net income and multiple it by 12 (months in the year),")
print("then divide that number by 52 (weeks in the year).")
print("The result: your available weekly net income is $", format(weekly_net_income, ".2f"))
#print("\nHopefully this helps you out. Knowing how much money you have free to spend can keep you out of trouble!")

##Inquires about regular savings account deposits and 401k
print("\nWhile calculating net income, we didn't consider whether you're regularly saving or have a 401k.")
savings_d=int(input("\nPlease enter the average deposit amount to savings: "))
savings_f=int(input("How many times per year are you making this deposit amount? "))
retirement=int(input("\nNext, how much are you paying into a 401k each year, on average, if any? "))
savings_annual=savings_d*savings_f
print("\nLet's take this new info and recalculate your net income.")
new_net=net_income-total_expenses-(savings_annual/12)-(retirement/12)
print("After accounting for your savings and 401k, your net income is $"+format(new_net, ".2f")+".")

print("\nYou've said that you deposit an average of $"+str(savings_d)+" "+str(savings_f)+" times per year,")
print("that brings your average annual savings to $"+str(savings_annual)+".")

if savings_annual > 0:
    print("\nGood job on saving up some money!")
else:
    print("Saving can be hard. Setting aside a couple dollars each month would be a great start.\n")
##Define function which calculates savings
def calculate_savings(annual):
    monthly_s=int(annual/12)
    while annual <= 120:
        annual=int(input("You can do better than that! Try again, and have faith in yourself! :"))
    return monthly_s
##Define function which calls to calculate_savings function
def main():
    savings_wanted=int(input("\nHow much would more you like to save over the next year? "))
    savings_needed=calculate_savings(savings_wanted)
    print("To save that much, you need to save an average of $" + format(savings_needed, ".2f")+ " each month.")
print("Whether you've saved or not, now is the time to make further effort--it's never too late.")
##Call to main function
main()
print("\nYou've said that you're paying $"+str(retirement)+" toward a retirement plan each year.")
if retirement > 0:
    print("Great job preparing for the future!")
else:
    print("Understandably, paying into a retirement account can be burdensome on finances. Good luck to you.")

print("\nWhat we haven't considered yet is your miscellaneous expenses (e.g., gym memberships or Netflix subscription.")
misc_exp=int(input("What are your average, normal monthly expenses on these types of items? "))
misc_annual=misc_exp*12
print("That makes your average annual expenditure on miscellaneous items $"+format(misc_annual, ".2f")+".")
print("\nKnowing what the costs of your miscellaneous expenses are, perhaps you can reevaluate your spending habits, ")
print("and consider shifting some of that spending toward savings.")
print("\nThanks for taking the time to use Josh's program. Hopefully you found it helpful.")

print("\nGood bye, "+ name.capitalize()+"!")
