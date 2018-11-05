class Unit:
    Units = {1:{0:'', 1:'m', 2:'cm', 3:'mm', 4:'km', 5:'ft', 6:'in'},
             2:{0:'', 1:'N', 2:'kN', 3:'kgf', 4:'lb', 5:'klb'},
             3:{0:'', 1:'kg', 2:'slug'}}
    def __init__(self):
        


class unit:
    def __init__(self,type='L',mult=0):
        self.check(type)    
        self.mult = mult;
        self.SI = 1
        self.pre()
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.LongName
    def check(self,type):
        SI = {'L': 'm', 'F': 'N', 'M': 'g','T':'°C','t':'s','s':'Pa'}
        SIL = {'L': 'meters', 'F': 'Newton', 'M': 'gramo','T':'°C','t':'second','s':'Pa'}

        if type in SI:
            self.type = type
        else:
            self.type = 'L'
            for clave, valor in SI.items():
                print(valor)
                if type is valor:   
                    self.type = clave        
        self.unit = SI[self.type]
        self.LongName = SIL[self.type]
        return 
    def pre(self):
        pre ={}
        if self.SI:
            pre['L'] = {-3:'m',-2:'c',0:'',3:'k'}
            pre['F'] = {0:'',3:'k'}
            pre['M'] = {0:'',3:'k'}    
            pre['s'] = {0:'',3:'k',6:'M',9:'G'}
        else:
            pass
        try:
            text = pre[self.type][self.mult]
        except KeyError:
            text =''
        self.name = text+self.unit


def cu(value):
    a = value.find(' ')
    val = value[0:a]
    uni = value[a+1:len(value)]
    print(val)
    print(uni)
class quantity:
    def __init__(self,value=0,U = unit()):
        if isinstance(value,str):
            a = value.find(' ')
            U = unit(value[a+1:len(value)])
            value = float(value[0:a])
            
        self.value = value
        self.unit = U
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

    
    


a = quantity('10.3 m')
c = quantity(20,unit('s',6))
b = quantity(25,unit('L',-3))
c = quantity(25,unit('L',-3))
print(a)
print(b)
print(a+b)

 

