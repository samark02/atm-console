class Admin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    def login(self, username, password):
        return self.username == username and self.password == password
    
    banks={}

    def add_bank(self,bankname,bankpass):
        self.banks[bankname]=bankpass

    def delete_bank(self,bankname):
        self.banks.pop(bankname)
    
    def view_banks(self):
        for i in self.banks:
            print(i)

class Customer:
    def __init__(self, name, acc_no, pin,balance, bankname):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        self.pin = pin
        self.bankname = bankname
    
    def check_balance(self):
        return f"Balance: {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} successfully deposited to you account\n Acc Balance: {self.balance}"
    
    def withdraw(self,amount):
        if amount>self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
            return f"{amount} Withdrawn\n Acc Balance: {self.balance}"
    
    def pin_change(self, new_pin, acc_no,bank):
        # self.pin = new_pin
        # bank=Bank()
        print(bank.customers[acc_no][3])
        bank.customers[acc_no][3] = new_pin
        return "Your Account pin has been successfully changed"

class Bank:
    def __init__(self):
        # self.bankname = bankname
        # self.bankpass = bankpass
        self.customers = {}

    def add_customer(self, customer):
        self.customers[customer.acc_no]=([customer.name,customer.acc_no,customer.balance,customer.pin,customer.bankname])

    def view_custs(self):
        print(self.customers)
        for customer in self.customers:
            print()
            print("Name:", self.customers[customer][0])
            print("Account Number:", self.customers[customer][1])
            print("Balance:", self.customers[customer][2])
            print("Bank:", self.customers[customer][4])
            print("PIN:", self.customers[customer][3])

    def find_customer(self, acc_no):
        for customer in self.customers:
            if customer == acc_no:
                return self.customers[customer]
        # return None

def main():
    bank = Bank()
    admin = Admin("admin","admin123")

    while True:
        print("\nWelcome to the ATM!")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Bank Login")
        print("4. Exit")

        ch = input("Enter your choice:")

        if ch == '1':
            username = input("Admin Username: ")
            password = input("Admin Password: ")
            
            if admin.login(username, password):
                print("Admin Logged In")

                while True:
                    print("\nAdmin Menu")
                    print("1. Add Customer")
                    print("2. View Customers")
                    print("3. Add Bank")
                    print("4. Delete Banks")
                    print("5. View Banks")
                    print("6. Exit")

                    ad_ch = input("Enter your choice: ")

                    if ad_ch == '1':
                        name = input("Enter customer name: ")
                        acc_number = input("Enter account number: ")
                        pin = input("Enter PIN: ")
                        if pin=='':
                            pin='0000'
                        bankname = input("Enter Bank Name:").upper()
                        if bankname=='':
                            bankname='HDFC'
                        customer = Customer(name, acc_number, pin, 0, bankname)
                        if bankname not in admin.banks:
                            admin.add_bank(bankname, bankname.lower())
                        bank.add_customer(customer)
                        print("Customer added successfully.")
                    elif ad_ch == '2':
                        bank.view_custs()
                    elif ad_ch == '3':
                        bankname = input("Enter Bank Name: ").upper()
                        bankpass = input("Enter Bank Password: ").lower()
                        if bankpass == "":
                            bankpass= bankname.lower()
                        admin.add_bank(bankname, bankpass)
                        print(f"{bankname} added successfully")
                    elif ad_ch == '4':
                        print("\nBank Closure")
                        bankname = input("Enter Bank Name: ")
                        admin.delete_bank(bankname.upper())
                        print(f"{bankname} closed successfully")
                    elif ad_ch == '5':
                        print("\nRegistered Banks:")
                        admin.view_banks()
                    elif ad_ch == '6':
                        print("Admin Logged Out")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid Credentials. Please try again")
        elif ch == '2':
            acc_no = input("Enter account number: ")
            pin = input("Enter PIN: ")
            cust = bank.find_customer(acc_no)
            print(cust[0],'---',cust[3],'----',pin)
            if cust[3] == pin:
                print(f"Welcome, {cust[0].capitalize()}!")
                while True:
                    print("\nCustomer Menu:")
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Pin Change")
                    print("5. Logout")

                    cust_ch = input("Enter your choice: ")

                    if cust_ch == "1":
                        print(customer.check_balance())
                    elif cust_ch == "2":
                        amount = float(input("Enter deposit amount: "))
                        print(customer.deposit(amount))
                    elif cust_ch == "3":
                        amount = float(input("Enter withdrawal amount: "))
                        print(customer.withdraw(amount))
                    elif cust_ch == "4":
                        pin = input("Enter your new PIN:")
                        print(customer.pin_change(pin,acc_no,bank))     
                    elif cust_ch == "5":
                        print("Customer logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("\nInvalid account number or PIN. Please try again.")
        elif ch == '4':
            print("\nThank you for using the ATM")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
