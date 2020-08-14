# Class Account ()
# Attributes: 
    # titular, is the owner of Account
    # balance, is the currently quantity of money in Accoun
  # Account.titular is required
  # Account.quantity is optional
# Methods: 
    # get(), 
    # set(), 
    # toString()
# Especial Methods
    # deposit(value) -> if value > 0 does nothing; 
    # withdraw(value) -> if withdraw() is executed and then .quantity < 0, then quantiy will be empty 


class Account:

    def __init__(self, titular, quantity):
        self.titular = titular
        self.quantity = quantity
    
    def get(self):
        print(f'Account: {self.titular}, Balance: {self.quantity} $COP')


class Execute():

    def __init__(self, account):
      self.account = account


if __name__ == "__main__":
    cuenta_jose = Account('JoseMelNet', 100)
    cuenta_jose.get()
