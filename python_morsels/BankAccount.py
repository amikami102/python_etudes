# BankAccount.py


class BankAccount:
    """
    A class representing a bank account.
    
    Attributes
    ----------
    _balance: int, default 0
        bank account's balance
    
    number: int
        unique bank account id
        
    _last_number: int
        keeps track of the next available unique account number
    
    accounts: list[BankAccount]
        a list of all `BankAccount` instances
            
    Methods
    -------
    deposit(amount: int)
        add positive amount of dollars to account balance;
        depositing negative amount will raise ValueError
        
    withdraw(amount: int)
        remove positive amount of dollars from account balance;
        removing negative amount or withdrawing more than account balance will
        raise ValueError
        
    transfer(other: BankAccount, amount: int)
        withdraw `amount` from one's balance and deposit
        to the other acount's balance
    """
    accounts: list = []
    _last_number: int = 1000
    
    def __init__(self, balance: int = 0) -> None:
        if balance < 0:
            raise ValueError(f'Cannot open account with {balance} balance')
        self._balance = balance
        self.number = BankAccount._last_number = BankAccount._last_number + 1
        BankAccount.accounts.append(self)	# add current instance to `accounts`
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}(balance={self.balance})"
    
    @property
    def balance(self) -> int:
        return self._balance
    
    def deposit(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f'Cannot deposit {amount}')
        self._balance += amount
    
    def withdraw(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f'Cannot withdraw {amount}')
        if amount > self.balance:
            raise ValueError(f'Cannot withdraw {amount} from {self.balance}')
        self._balance -= amount
    
    def transfer(self, other: 'BankAccount', amount: int) -> None:
        self.withdraw(amount)
        other.deposit(amount)


# base problem
a1 = BankAccount()
assert a1.balance == 0
a1.deposit(10)
assert a1.balance == 10
a2 = BankAccount(balance=20)
a2.withdraw(15)
assert a2.balance == 5
a1.transfer(a2, 3)
assert repr(a1) == 'BankAccount(balance=7)'

# bonus 1, make sure negative amounts cannot be withdraw, deposited, or transferred
try:
    BankAccount(-10)
except ValueError:
    print('passed setting up negative balance account')
a1 = BankAccount(10)
try:
    a1.withdraw(-5)
except ValueError:
    print('passed withdrawing negative value')
try:
    a1.withdraw(50)
except ValueError:
    print('passed withdrawing more than account balance amount')
try:
    a1.deposit(-5)
except ValueError:
    print('passed depositing negative value')
try:
    a2 = BankAccount(balance=20)
    a1.transfer(a2, 100)
except ValueError:
    print('passed transfering more than account balance')

# bonus 2, test assigning unique account number
BankAccount.accounts.clear()
a1 = BankAccount(100)
a2 = BankAccount()
assert a1.number != a2.number
a3 = BankAccount(50)
assert a3.number != a2.number
# test that `BankAccount` class keeps track of all opened accounts
assert len(BankAccount.accounts) == 3
assert BankAccount.accounts[0].balance == 100
assert BankAccount.accounts[2].balance == 50
a1.transfer(a3, 15)
assert BankAccount.accounts[0].balance == 100 - 15
assert BankAccount.accounts[2].balance == 50 + 15

# bonus 3, test that `balance` is read-only attribute
a1 = BankAccount(100)
assert a1.balance == 100
try:
    a1.balance = 500
except AttributeError:
    print('passed overwriting balance attribute')
assert a1.balance == 100
a1.deposit(400)
assert a1.balance == 500