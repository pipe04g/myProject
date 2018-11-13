class Unit:
    
    Units = {0:{0:'', 1:'m', 2:'cm', 3:'mm', 4:'km', 5:'ft', 6:'in'},
             1:{0:'', 1:'N', 2:'kN', 3:'kgf', 4:'lb', 5:'klb'},
             2:{0:'', 1:'kg', 2:'slug'},
             3:{0:'', 1:'seg'},
             4:{0:'', 1:'°C', 2:'°F'},
             5:{0:'', 1:'Pa', 2:'kPa', 3:'MPa', 4:'psi', 5:'ksi'}
             }

    
    def __init__(self,text = '',code=[]):
        if code ==[]:
            if text !='':
                self.code = self.coding(text)
            else:
                self.code = self.codedef()
        else:
            self.code = code
    def check(self):
        code = self.code
        if (code[0][1]==1 and code[1][1]==1)and(code[0][0]==1 and code[1][0]==-2):
            for x in range(0,2):
                for y in range(0,2):
                    code[x][y]=0
            code[0][5] = 1 
            code[1][5] = 1
            
    
    def __str__(self):
        return self.forcode(self.code)

    __repr__ = __str__

    def coding(self,text):
        code = self.codedef()
        text = text.split('/');
        for x in range(0,len(text)):
            textx = text[x].split();
            for a in textx:
                n = 1-2*x                    
                if a[-1].isdigit():
                    n = int(a[-1])*n
                    a = a[:-1]
                for key in self.Units:
                    for u in self.Units[key]:
                        if self.Units[key][u] == a:
                            code[0][key]= u
                            code[1][key]= n
                            break
        return code

    def forcode(self,code):
        U = self.Units;
        text = '';
        text2 = '';
        for x in range(0,len(U)):
            n = '';
            if abs(code[1][x])>1:
                n = str(abs(code[1][x]))
            if code[1][x]>0:
                text += ' '+U[x][code[0][x]]+str(n);
            elif code[1][x]<0:
                text2 += ' '+U[x][code[0][x]]+str(n);
        if text2 != '':
            text += ' /' + text2
        return text
    def codedef(self):
        return [[0]*len(self.Units),[0]*len(self.Units)]
    
    def __mul__(self,a):        
        if type(a) is Unit:
            ans = self.codedef()
            for x in range(0,len(ans[0])):
                if self.code[0][x] == a.code[0][x]:
                    ans[0][x] = a.code[0][x]
                    ans[1][x] = a.code[1][x] + self.code[1][x]
                else:
                    if a.code[0][x]!=0:
                        ans[0][x] = a.code[0][x]
                    else:
                        ans[0][x] = self.code[0][x]
                    ans[1][x] = a.code[1][x] + self.code[1][x]
            ans = Unit(code= ans)
                    

        else:
            # Cambiar para que sea como un error.......
            print('The second argument is not a Unit')
            return
        return ans
    
            
            
                        
a = '0123/456';
a = a.split('/');
for x in range(0,2):
    print(a[x])
        

ab = Unit()
ac = Unit()
ab.code[0][1]=1
ab.code[1][1]=1
ab.code[0][0]=1
ab.code[1][0]=-2
ab.code

ac.code[0][0]=1
ac.code[1][0]=2
print(ab)

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

 

