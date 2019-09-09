if __name__ == '__main__':
    class BankAccount:
        def __init__(self, bank, account_name, account_balance):
            self.bank = bank
            self.account_name = account_name
            self.account_balance = account_balance


    data_list = input().split(' | ')

    bank_accounts_list = []

    while not data_list[0] == 'end':
        bank_name = data_list[0]
        input_account_name = data_list[1]
        input_account_balance = float(data_list[2])

        bank_account = BankAccount(bank=bank_name, account_name=input_account_name,
                                   account_balance=input_account_balance)

        bank_accounts_list.append(bank_account)
        data_list = input().split(' | ')

    for bank_account in sorted(bank_accounts_list, key=lambda acc: (-acc.account_balance, len(acc.bank))):
        print(f'{bank_account.account_name} -> {bank_account.account_balance:.2f} ({bank_account.bank})')
