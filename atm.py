balance=5000
option = input("Enter your option:/npress '1' for withdrawl/n press '2' for deposit/ n press '3' for check balance/n press '4' for exit")
while true:
    print("enter your option")
    if option == '1':
        withdrawl = int(input("Enter the amount to withdrawl:"))
        if withdrawl > balance:
            print("insufficient balance")
            break
        else:
            balance -= withdrawl
            print("withdrawl successful")
            print("your current balance is:",balance)
            break
    elif option=='2':
        deposit = int(input("Enter the amount to deposit:"))
        balance += deposit
        print("deposit successful")
        print("your current balance is:",balance)
        break
    elif option=='3':
        print("your current balance is:",balance)
        break
    else:
        print("invalid option")

