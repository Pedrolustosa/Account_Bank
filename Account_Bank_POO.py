import textwrap

class User:
    def __init__(self, name, cpf, date_of_birth, address):
        self.name = name
        self.cpf = cpf
        self.date_of_birth = date_of_birth
        self.address = address


class Account:
    def __init__(self, branch, account_number, user):
        self.branch = branch
        self.account_number = account_number
        self.user = user
        self.balance = 0
        self.statement = ""
        self.num_withdrawals = 0
        self.limit = 500
        self.withdrawal_limit = 3

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.statement += f"Deposit:\tR$ {amount:.2f}\n"
            print("\n=== Deposit successful! ===")
        else:
            print("\n@@@ Operation failed! The specified amount is invalid. @@@")

    def withdraw(self, amount):
        exceeded_balance = amount > self.balance
        exceeded_limit = amount > self.limit
        exceeded_withdrawals = self.num_withdrawals >= self.withdrawal_limit

        if exceeded_balance:
            print("\n@@@ Operation failed! You do not have sufficient balance. @@@")

        elif exceeded_limit:
            print("\n@@@ Operation failed! The withdrawal amount exceeds the limit. @@@")

        elif exceeded_withdrawals:
            print("\n@@@ Operation failed! Maximum number of withdrawals exceeded. @@@")

        elif amount > 0:
            self.balance -= amount
            self.statement += f"Withdrawal:\tR$ {amount:.2f}\n"
            self.num_withdrawals += 1
            print("\n=== Withdrawal successful! ===")

        else:
            print("\n@@@ Operation failed! The specified amount is invalid. @@@")

    def display_statement(self):
        print("\n================ STATEMENT ================")
        print("No transactions were made." if not self.statement else self.statement)
        print(f"\nBalance:\t\tR$ {self.balance:.2f}")
        print("============================================")


def menu():
    menu_text = """\n
    ================ MENU ================
    [d]\tDeposit
    [s]\tWithdraw
    [e]\tStatement
    [nc]\tNew account
    [lc]\tList accounts
    [nu]\tNew user
    [q]\tQuit
    => """
    return input(textwrap.dedent(menu_text))


def create_user():
    cpf = input("Enter the CPF (numbers only): ")
    name = input("Enter the full name: ")
    date_of_birth = input("Enter the date of birth (dd-mm-yyyy): ")
    address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")

    return User(name, cpf, date_of_birth, address)


def create_account(users):
    cpf = input("Enter the CPF of the user: ")
    user = next((user for user in users if user.cpf == cpf), None)

    if user:
        account_number = len(accounts) + 1
        branch = "0001"
        account = Account(branch, account_number, user)
        accounts.append(account)
        print("\n=== Account created successfully! ===")
    else:
        print("\n@@@ User not found, account creation flow continues! @@@")
        name = input("Enter the full name of the user: ")
        date_of_birth = input("Enter the date of birth (dd-mm-yyyy): ")
        address = input("Enter the address (street, number - neighborhood - city/state abbreviation): ")
        user = User(name, cpf, date_of_birth, address)
        users.append(user)
        create_account(users)



def list_accounts():
    for account in accounts:
        line = f"""\
            Branch:\t\t{account.branch}
            A/C:\t\t{account.account_number}
            Holder:\t\t{account.user.name}
        """
        print("=" * 100)
        print(textwrap.dedent(line))


def main():
    global accounts
    accounts = []
    users = []

    while True:
        option = menu()

        if option == "d":
            amount = float(input("Enter the deposit amount: "))
            account = accounts[0] if accounts else None
            if account:
                account.deposit(amount)
            else:
                print("\n@@@ No account available! Create an account first. @@@\n")

        elif option == "s":
            amount = float(input("Enter the withdrawal amount: "))
            account = accounts[0] if accounts else None
            if account:
                account.withdraw(amount)
            else:
                print("\n@@@ No account available! Create an account first. @@@\n")

        elif option == "e":
            account = accounts[0] if accounts else None
            if account:
                account.display_statement()
            else:
                print("\n@@@ No account available! Create an account first. @@@\n")

        elif option == "nu":
            users.append(create_user())

        elif option == "nc":
            create_account(users)

        elif option == "lc":
            list_accounts()

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")


if __name__ == "__main__":
    main()
