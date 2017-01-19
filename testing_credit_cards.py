from CreditCard import CreditCard

wallet = CreditCard('Lateema Spencer', 'California Savings', '5391 0375 9387 5309', 100)
print('Customer =', wallet.get_customer())
print('Bank =', wallet.get_bank())
print('Account =', wallet.get_account())
print('Limit =', wallet.get_limit())
print('Balance =', wallet.get_balance())
while wallet.get_balance() > 100:
    wallet.make_payment(100)
    print('New Balance =', wallet.get_balance())
print()
