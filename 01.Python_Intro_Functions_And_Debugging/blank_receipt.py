def print_dashes():
    print('------------------------------')


def print_header():
    print('CASH RECEIPT')
    print_dashes()


def print_body():
    print('Charged to____________________\nReceived by___________________')


def print_footer():
    print_dashes()
    print('© SoftUni')


def print_receipt():
    print_header()
    print_body()
    print_footer()


if __name__ == '__main__':
    print_receipt()
