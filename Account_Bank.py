def deposit(saldo):
    try:
        value = float(input("Enter the deposit amount: "))
        if value > 0:
            saldo += value
            print(f"Deposit of $ {value:.2f} completed successfully.")
        else:
            print("Operation failed! The entered value is invalid.")
    except ValueError:
        print("Operation failed! Invalid value.")

    return saldo

def withdraw(saldo, limit, num_withdrawals):
    MAX_WITHDRAWALS = 3
    try:
        value = float(input("Enter the withdrawal amount: "))

        if value <= 0:
            print("Operation failed! The entered value is invalid.")
        elif value > saldo:
            print("Operation failed! You don't have enough balance.")
        elif value > limit:
            print("Operation failed! The withdrawal amount exceeds the limit.")
        elif num_withdrawals >= MAX_WITHDRAWALS: # type: ignore
            print("Operation failed! Maximum number of withdrawals exceeded.")
        else:
            saldo -= value
            print(f"Withdrawal of $ {value:.2f} completed successfully.")
            num_withdrawals += 1
    except ValueError:
        print("Operation failed! Invalid value.")

    return saldo, num_withdrawals

def display_statement(saldo, statement):
    print("\n================ STATEMENT ================")
    print("No transactions have been made." if not statement else statement)
    print(f"\nBalance: $ {saldo:.2f}")
    print("============================================")

def main():
    saldo = 0
    limit = 500
    statement = ""
    num_withdrawals = 0

    menu = """
    [d] Deposit
    [w] Withdraw
    [s] Statement
    [q] Quit

    => """

    while True:
        option = input(menu)

        if option == "d":
            saldo = deposit(saldo)
            statement += f"Deposit: $ {saldo:.2f}\n"

        elif option == "w":
            saldo, num_withdrawals = withdraw(saldo, limit, num_withdrawals)
            statement += f"Withdrawal: $ {saldo:.2f}\n"

        elif option == "s":
            display_statement(saldo, statement)

        elif option == "q":
            break

        else:
            print("Invalid operation, please select the desired operation again.")

if __name__ == "__main__":
    main()
