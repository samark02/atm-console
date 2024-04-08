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
            print(i.name)

class Customer:
    def __init__(self, name, acc_no, balance, pin=0000, bankname='HDFC'):
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
    
    def pin_change(self, new_pin):
        self.pin = new_pin
        return "Your Account pin has been successfully changed"

class Bank:
    def __init__(self,bankname, bankpass):
        self.bankname = bankname
        self.bankpass = bankpass
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def view_custs(self):
        for customer in self.customers:
            print("Name:", customer.name)
            print("Account Number:", customer.acc_no)
            print("Balance:", customer.balance)
            print()

    def find_customer(self, account_number):
        for customer in self.customers:
            if customer.account_number == account_number:
                return customer
        # return None

def main():
    bank = Bank("HDFC","hdfc")
    admin = Admin("admin","admin123")

    while True:
        print("\nWelcome to the ATM!")
        print("1. Admin Login")
        print("2. Customer Login")
        print("3. Bank Login")
        print("4. Exit")

        ch = int(input("Enter your choice:"))

        if ch == 1:
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

                    ad_ch = int(input("Enter your choice: "))

                    if ad_ch == 1:
                        name = input("Enter customer name: ")
                        acc_number = input("Enter account number: ")
                        pin = input("Enter PIN: ")
                        bankname = input("Enter Bank Name:").upper()
                        customer = Customer(name, acc_number, pin, 0, bankname)
                        if bankname not in admin.banks:
                            admin.add_bank(bankname, bankname.lower())
                        bank.add_customer(customer)
                        print("Customer added successfully.")
                    elif ad_ch == 2:
                        bank.view_custs()
                    elif ad_ch == 3:
                        bankname = input("Enter Bank Name: ").upper()
                        bankpass = input("Enter Bank Password: ").lower()
                        if bankpass == "":
                            bankpass= bankname.lower()
                        admin.add_bank(bankname, bankpass)
                        print(f"{bankname} added successfully")
                    elif ad_ch == 4:
                        print("\nBank Closure")
                        bankname = input("Enter Bank Name: ")
                        admin.delete_bank(bankname)
                        print(f"{bankname} closed successfully")
                    elif ad_ch == 5:
                        print("\nRegistered Banks")
                        admin.view_banks()
                    elif ad_ch == 6:
                        print("Admin Logged Out")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid Credentials. Please try again")
        elif ch == 2:
            acc_number = input("Enter account number: ")
            pin = input("Enter PIN: ")
            customer = bank.find_customer(acc_number)
            if customer and customer.pin == pin:
                print(f"Welcome, {customer.name}!")
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
                        new_pin = int(input("Enter your new PIN:"))
                        print(customer.pin_change(new_pin))                        
                    elif cust_ch == "5":
                        print("Customer logged out.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Invalid account number or PIN. Please try again.")
        elif ch == 4:
            print("Thank you for using the ATM")
            break

if __name__ == "__main__":
    main()