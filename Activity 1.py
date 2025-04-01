#Private Variable and Method
class MyClass:
    __PrivateVar = 27 #Private Variable
    
    def __PrivateMeth(): #Private Mathod
        print('This is the private class')
        
    def Hello(self):
        print('This is a normal method')
        print('The value of the private method is :',MyClass.__PrivateVar)
        
foo = MyClass()
#foo.__PrivateMeth() 
foo.Hello()