##Joshua Penn
##COP 1500 - Integration Project
##Application to assist with budgeting monthly finances

print("Welcome to Josh's Python Integration Project.")
print("May I have your name, please?")
name = input()
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
rent: int = int(input("\nNext, please enter your monthly rent expense amount : "))
if rent <= 500:
    print("\nWow! Great job on finding inexpensive rent!!")
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
print("\nYour monthly income is $", income)
total_expenses = (rent + car + insurance + gas + food + cell)
print("Your total monthly expenses are $", total_expenses)
proceed = input("\nPress the ENTER key to continue...")

##Calculate and display monthly net income
print("\nNext, we'll calculate your net income. Net income is the difference between your income and expenses.")
print("Another way to look at it, is that it's how much money you have left after paying your expenses.")
net_income = (income - total_expenses)
print("Your monthly net income is $", net_income)
print("\nNow that you know your net income, you have an idea about how much you money you have available each month.")
print("Let's take it a bit further though and see what your average available net income is each week,")
print("as that will make it easier for you to budget successfully.\n")
proceed = input("\nPress the ENTER key to continue...")

##Calculate and display weekly net income
weekly_net_income = (net_income * 12 / 52)
print("\nTo do this calculation, we take your monthly net income and multiple it by 12 (months in the year),")
print("then divide that number by 52 (weeks in the year).")
print("The result: your available weekly net income is $", format(weekly_net_income,'.2f'))
print("\nHopefully this helps you out. Knowing how much money you have free to spend can keep you out of trouble!")
print("\nGood bye, "+ name.capitalize()+"!")
