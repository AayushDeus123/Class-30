#Point Function
class Point:
    def __init__(self,x = 1 , y = 0):
        self.y = y
        self.x = x
    
    def __str__(self):
        return '({0},{1})'.format(self.x , self.y)
    
p1 = Point(2, 3)
print(p1)