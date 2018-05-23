class unit:
    def __init__(self,type='L',mult=0):
        self.type = type
        self.mult = mult;
        self.SI = 1
        self.check()
        self.pre()
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.LongName
    def check(self):
        SI = {'L': 'm', 'F': 'N', 'M': 'g','T':'°C','t':'s','s':'Pa'}        
        self.unit = SI[self.type]
        self.LongName = 'meters'
        return 
    def pre(self):
        pre ={}
        if self.SI:
            pre['L'] = {-3:'m',-2:'c',0:'',3:'k'}
            pre['F'] = {0:'',3:'k'}
            pre['M'] = {0:'',3:'k'}            
            pre['T'] = {0:''}            
            pre['t'] = {0:''}
            pre['s'] = {0:'',3:'k',6:'M',9:'G'}
        else:
            pre['L'] = {0:''}
        self.name = pre[self.type][self.mult]+self.unit



class quantity:
    def __init__(self,value=0,unit = unit()):
        self.value = value
        self.unit = unit
    def m(self):
        return self.unit.mult
    def e(self):
        return self.value*10**self.m()
    def __str__(self):
        return "%s %s" % (self.value, self.unit)
    def uType(self):
        return self.unit.type
    __repr__ = __str__  
    def __add__(self, a):
        if type(a) is quantity:
            if self.uType() is a.uType():
                m1 = self.m()
                m2 = a.m()
                if m1>m2:
                    m = m1
                    unit = self.unit
                else:
                    m = m2
                    unit = a.unit
                value = self.e()+a.e()
                value = eval("%fe%d"% (value,-m))
                ans = quantity(value,unit)
            else:
                print('The quantities have diferents units')
                return
        else:
            ans = quantity(self.value+a,self.unit)
        return ans
    __radd__ = __add__      
    def __sub__(self,B):
        return ans

    
    


a = quantity(10.3)
c = quantity(20,unit('s',6))
b = quantity(25,unit('L',-3))
print(a)
print(b)
print(a+b)
 

