class Acc:
 def __init__(self,id,balance):
  self.id=id
  self.bal=balance
 
  def withdraw(self,amt):
   if amt< self.bal:
     self.bal-=amt
     print("Amount %d withdrawn"%amt)
  def deposit(self ,amt):
   self.bal+=amt
   print("Amount %d deposited"%amt)

class SavAcc(Acc):
  minbal=1000
  def __init__(self,id,balance):
    super().__init__(id,balance)
  def withdraw(self , amt):
   if self.bal-amt >= SavAcc.minbal:
     super().withdraw(amt)
     print("Amount %d withdrawn"%amt)



savAcc=SavAcc("10023",10000)
savAcc.withdraw(2000)
print("Left amount:", savAcc.bal)










"""
BankAccount
Accid
minbal
balance
wihtdraw(amount)
deposit(amount ,Accid)

SavingsAccount
when withdrawing from Savings account min balance check should be made


SalaryAccount
depositer

when depositing to savings account , the depositer accountid should be  checked , nobody else is allowed to 
deposit into SalaryAccount



InsurancePlan
-Health Insurance , Life Insurance , PropertyInsurance
"""
