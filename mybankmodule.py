from cgi import print_directory
import random
dict_account = {}


def create_account(name,password):
    dict_account[name] = {}
    dict_account[name][name] = password
    print("Account created successfully!....")
    account_number = str(round(random.random(), 10))[2:]
    pin_number = str(round(random.random(), 4))[2:]
    dict_account[name]["balance"] = 0.0
    dict_account[name]["Account_number"] = account_number
    dict_account[name]["pin"] = pin_number
    print("Account Number is ",account_number)
    print("the pin is ",pin_number)

def login(name, password):
    if name in dict_account and dict_account[name][name] == password :
        print("welcome User")
        return True
    else :
        print("Invalid User")
        return False

def AddBalance(name):
    amount = float(input("Enter the amount to add : "))
    balance = dict_account[name]['balance']
    dict_account[name]['balance'] = amount + balance


def ViewBalance(name):
    balance = dict_account[name]['balance']
    print(f'balance is{balance}')    

def Transaction(name,pin):
    if dict_account[name]['pin'] == pin:
        amount = float(input("enter the amount to Withdraw : "))
        balance = dict_account[name]['balance']
        if balance > amount:
            print("balance is ", balance - amount)
            balance = balance - amount 
            dict_account[name]['balance'] = balance
        else:
            print(" Insufficient Balance ")
    else:
        print("Invalid PIN")            
