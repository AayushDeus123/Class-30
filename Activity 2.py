class Computer:
    def __init__(self):
        self.__maxprice = 900
        
    def Sell(self):
        print('Selling Price : {}'.format(self.__maxprice))
        
    def SetMaxPrice(self,price):
        self.__maxprice = price
        
c = Computer()
c.Sell()
c.__maxprice = 1000
c.Sell()

#Accessing the Private Variable
c.SetMaxPrice(1000)
c.Sell()