from abc import ABC,abstractmethod
class TransferFunds(ABC):
    def __init__(self,ac_no,bal):
        self.__ac_no=ac_no
        self.__bal=bal
    @property
    def account_no(self):
        return self.__ac_no
    @property
    def balance(self):
        return self.__bal
    @balance.setter
    def balance(self,bal):
        self.__bal=bal
    @abstractmethod
    def transfer(self,amt):
        pass
    def validate(self):
        if len(str(self.__ac_no))>10 and self.__bal>0:
            return True
        return False
class NftTransfer(TransferFunds):
    charges=0.05
    def __init__(self,ac_no,bal):
        super().__init__(ac_no,bal)
        self.validate()
    def transfer(self,amt):
        charges=amt*(NftTransfer.charges)
        tot_amt=amt+charges
        if self.balance>tot_amt:
            self.balance=self.balance-tot_amt
            print("Transaction commited successfully")
            print("amount:",amt)
            print("charges:",charges)
            print("tot_amt:",tot_amt)
            print("your account balance",self.balance)
        else:
            print("you don't have enough money")
    @classmethod
    def update_charges(cls,val):
        cls.charges=val

#rgts
class RgtsTransfer(TransferFunds):
    charges=0.02
    def __init__(self,ac_no,bal):
        super().__init__(ac_no,bal)
        self.validate()
    def transfer(self,amt):
        charges=amt*(RgtsTransfer.charges)
        tot_amt=amt+charges
        if self.balance>tot_amt:
            self.balance=self.balance-tot_amt
            print("Transaction commited successfully")
            print("amount:",amt)
            print("charges",charges)
            print("tot_amt",tot_amt)
            print("your account balance",self.balance)

        else:
            print("you don't have enough money")
    @classmethod
    def update_charges(cls,val):
        cls.charges=val



def main():
    ac_no=int(input("enter your account number:"))
    bal=int(input("enter your account balance:"))
    print("select type of transfer:")
    print("1. NFT transfer")
    print("2. Rgts transfer")
    trans_type=int(input("enter your choice:"))
    trans_amt=int(input("enter your transfer amount:"))
    if trans_type==1:
        ref=NftTransfer(ac_no,bal)
        ref.transfer(trans_amt)
    elif trans_type==2:
        ref=RgtsTransfer(ac_no,bal)
        ref.transfer(trans_amt)
main()