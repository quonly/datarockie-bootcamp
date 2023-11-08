class ATM:
  """
  The simple ATM class. In this class you need to specify name and pin.
  """

  def __init__(self, name, pin):
    self.name = name
    self.pin = int(pin)
    self.balance = 0

  def deposit(self, money):
    self.balance += money

  def withdraw(self, money):
    if money > self.balance:
      print("You can withdraw money greather than you have.")

    else:
      authorize = self.authorize()
      if not authorize:
        print("Your PIN is wrong. please try again.")
        return
      self.balance -= money
      print(f"Withdraw: {money}\nYour balance is {self.balance}")

  def authorize(self):
    """
    This method call when use withdraw method. You need to provide PIN to console to continue running.
    """
    pin = input("Your PIN: ")
    if int(pin) == self.pin:
      return True

  def display_balance(self):
    print(f"Balance: {self.balance}")

  def change_pin(self):
    pin = input("enter your new pin: ")
    self.pin = int(pin)
    print("you changed pin")


if __name__ == '__main__':
  atm = ATM("Mos", 1234)
  atm.deposit(5000)
  atm.display_balance()
  atm.withdraw(500)
  atm.display_balance()
  atm.change_pin()
