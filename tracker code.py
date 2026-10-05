from datetime import datetime 

# Expense Tracker Project 

expensesList = [] #list of expenses stores in format of dictionary 
print(" Welcome to Expense Tracker : ")

while True:
    print("====MENU====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending ")
    print("4. Exit")

    choice= int(input("Please Enter Choice : "))

#ADD Expense
    if(choice == 1):
        date= datetime.strptime(input("What is the spent expensive date (MM/DD/YYYY) ?: "), "%m/%d/%Y") 
        category= input("What category it belongs to ? (Food, Travel, Housing, Books, More.. ): ")
        description= input("More About the Expenses: ")
        amount= float(input("Enter the amount spent: "))

        expense= {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }

        expensesList.append(expense)
        print(" \n DONE . One Expense is Saved succesfully")

# 2. VIEW ALL EXPENSES 
    elif(choice == 2):
        if( len(expensesList)==0 ):
            print("No Expenses Added. ")
        else:
           print("====== details of expenses ======")
           count= 1
           for each in expensesList:
                print(f"Expense Number {count} -> Date: {each["date"]}, Category: {each["category"]}, Description: {each["description"]}, Amount: {each["amount"]} ")
                count= count+1

# 3. View Total Spending 
    elif(choice == 3):
        total= 0
        for every in expensesList:
            total = total + every["amount"]

        print("\n TOTAL SPEND = ", total)

#4. EXIT 
    elif(choice == 4):
        print("THANK YOU FOR USING.... ")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
