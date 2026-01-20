class ATM:

    def __init__(self):
        self.pin = None
        self.balance =0
        self.menu()

    def menu(self):
        user_input = input("""
        Hi how can I help you?
        1. Press 1 to create PIN
        2. Press 2 to change PIN
        3. Press 3 to check balance
        4. Press 4 to withdraw
        5. Anything else to exit 
        Enter here : """)

        if user_input == '1' :
            self.create_pin()
        
        elif user_input =='2':
            self.change_pin()

        elif user_input=='3':
            self.check_balance()

        elif user_input=='4':
            self.withdraw()

        else:
            exit()

    def create_pin(self):
        user_pin = int(input("Create your PIN : "))
        self.pin = user_pin

        user_balance = int(input('Enter initial balance:'))
        self.balance = user_balance

        print("pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = int(input("Enter your old PIN : "))
        if old_pin==self.pin:
            new_pin = int(input("Enter new PIN : "))
            self.pin = new_pin
            
            print('PIN change successful')
            self.menu()
        else:
            print('Invalid PIN')
            self.menu()

    def check_balance(self):
        use_pin = int(input("Enter your PIN : "))
        if use_pin == self.pin:
            print('Your balance is - ', self.balance)
            self.menu()
        else:
            print('Invalid PIN ')
            self.menu()

    def withdraw(self):
        user_pin = int(input("Enter your PIN : "))
        if user_pin==self.pin:
            amount = int(input("Enter amount : "))
            if amount<=self.balance:
                self.balance = self.balance- amount
                print('Withdrawal successful. Balance is ',self.balance)
            else:
                print('Insufficient balance!')
            self.menu()
        else:
            print("Invalid PIN!")
            self.menu()

user = ATM()
user