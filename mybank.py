import mybankmodule as bank

print("Welcome to my bank")

while True:
    print("C to create account")
    print("L to login")
    print("v to view users")
    print("Q to Exit")
    user_input = input("Enter the Key : ")
    if  user_input.upper() == 'C' :
        user_name = input("Enter the Name : ")
        user_password = input("Enter the Password : ")
        bank.create_account(user_name, user_password)
    elif user_input.upper()  == 'L':
        name = input("Enter the username  : ")
        password = input("Enter the Password : ")
        if bank.login(name , password):
            while True:
                print("Press T to Withdraw ")
                print("Press A to Add Balance ")
                print("Press V to View Balance ")
                print("Press Q to Exit ")
                user_input = input("Press Key : ")
                if user_input.upper() == 'T':
                        pin = input("Enter PIN : ")
                        bank.Transaction(name,pin)
                elif user_input.upper() == 'A': 
                        bank.AddBalance(name)
                elif user_input.upper() == 'V':
                        bank.ViewBalance(name)
                elif user_input.upper() == 'Q':
                        break
    elif user_input.upper() == 'Q':
            break            


           
