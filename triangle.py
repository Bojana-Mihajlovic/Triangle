class Triangle (): 
    def __init__ (self,a,b,c):
        self.a = float (a)
        self.b = float (b)
        self.c = float (c) 
    def is_valid(self):
        if (self.a + self.b)>self.c and (self.c + self.b)>self.a and (self.a + self.c)>self.b: 
            return True 
        else: 
            return False 
    def area(self): 
            s = (self.a+ self.b+self.c)/2
            if s - self.a >= 0 and s - self.b >= 0 and s - self.c >= 0:
                return (s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5 
    def perimeter(self): 
            if (self.a + self.b)>self.c and (self.c + self.b)>self.a and (self.a + self.c)>self.b:
                return self.a + self.b + self.c
    def scale (self, scale_factor):
        return Triangle(scale_factor*self.a, scale_factor*self.b, scale_factor*self.c)

    def is_right(self): 
        if (self.a**2 + self.b**2 == self.c**2) or (self.c**2 + self.b**2 == self.a**2) or (self.a**2 + self.c**2 == self.b**2):
            return True 
        else: 
            return False 

t = Triangle (3,3,3)

print (t.is_valid())
print (t.is_right()) 
print (t.area()) 
print (t.perimeter())



