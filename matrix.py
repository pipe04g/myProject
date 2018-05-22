#from matrix import *
def size(self):
        return self.m,self.n

def transpose(self):
        value = zeros(self.n, self.m)
        i = 0
        for row in self.data:
                j = 0
                for val in row:
                        value.data[j][i] = val
                        j = j + 1
                i = i + 1               
        return value
        
def zeros(m,n):
        ans = matrix(0,m,n)
        return ans
                       
def det(self):
        ans = 0
        m = self.m
        n = self.n
        if m != n:
                raise TypeError('Matrix must be square')
        if m == 2:
                ans = self(1,1)*self(2,2)-self(1,2)*self(2,1)
        if m > 2:
                i=0
                for j in range(0,n):
                        mv = list(range(1,m+1))
                        nv = list(range(1,m+1))
                        mv.pop(i)                        
                        nv.pop(j)
                        b = self.ind(mv,nv)
                        ans += det(b)*self(i+1,j+1)*(1-2*(j%2))                               
        return ans

def inv(self): 
        m = self.m
        n = self.n
        ans = zeros(m,n)
        if m != n:
                raise TypeError('Matrix must be square')
        if m == 2:
                ans.data[0][0] = self(2,2)
                ans.data[0][1] = -self(1,2)
                ans.data[1][0] = -self(2,1)
                ans.data[1][1] = self(1,1)
        
        if m > 2:
                mt = transpose(self)
                for i in range(0,m):
                        for j in range(0,n):
                                mv = list(range(1,m+1))
                                nv = list(range(1,n+1))
                                mv.pop(i)                        
                                nv.pop(j)
                                b = mt.ind(mv,nv)
                                ans.data[i][j] = det(b)*(1-2*(j%2))*(1-2*(i%2))
        d=(1/det(self))
        ans = ans*d
        return ans

def diag(self):
        if type(self) is matrix:         
                ans = []
                i = 0
                for x in self.data:
                        ans.append(x[i])
                        i+=1
        if type(self) is list:
                m = len(self)
                ans = zeros(m,m)
                i = 0
                for x in self:
                        ans.data[i][i] = x
                        i+=1
        return ans

def eye(m,n = None):
        if n == None:
                n = m        
        ans = zeros(m,n)
        for x in range(0,m):
                 ans.data[x][x] = 1
        return ans
def m(M):
        ans = matrix(M)
        return ans
def sum(self):
        m = self.m
        n = self.n
        if m == 1:
                ans = 0
                for x in self.data[0]:
                        ans += x
        elif n == 1:
                ans = 0
                for x in self.data:
                        ans += x[0]
        else:
                ans = zeros(1,n)
                for i in range(0,m):
                        for j in range(0,n):
                                ans.data[0][j] += self.data[i][j]
        return ans

class matrix:
        def __init__(self,M = None,m = None,n = None):            
                self.data = M
                self.m = m
                self.n = n
                if m != None:
                        if n != None:
                                self.data = []
                                for x in range(0, m):
                                        self.data.append([])
                                        for y in range(0,n):
                                                self.data[x].append(M)
                if M != None:
                        if type(M) is list:
                                self.m = len(M)
                                if type(M[0]) is list:
                                        self.n = len(M[0])
                                elif type(M[0]) is int:
                                        self.n =1;
                                dimen = 1;
                                for row in M:
                                        if type(row) is list:
                                                nrow = len(row)
                                        else:
                                                nrow =1
                                        if self.n != nrow:      
                                                dimen = 0
                                if dimen == 0:
                                        raise TypeError('Dimensions mismatch')
                self.act()
        def __add__(self, B):
                ans = matrix(0,self.m,self.n)
                for i in range(0, self.m):
                        for j in range(0, self.n):
                                if type(B) is int:
                                        C = B
                                else:
                                        C = B.data[i][j]
                                ans.data[i][j] = self.data[i][j]+C
                return ans      
        
        def __sub__(self,B):
                ans = matrix(0,self.m,self.n)
                for i in range(0, self.m):
                        for j in range(0, self.n):
                                if type(B) is int:
                                        C = B
                                else:
                                        C = B.data[i][j]
                                ans.data[i][j] = self.data[i][j]-C
                return ans
        
        def __rsub__(self,B):
                ans = matrix(0,self.m,self.n)
                for i in range(0, self.m):
                        for j in range(0, self.n):
                                if type(B) is int:
                                        C = B
                                else:
                                        C = B.data[i][j]
                                ans.data[i][j] = C-self.data[i][j]
                return ans
                
        def __neg__(self):
                ans = matrix(0,self.m,self.n)
                for i in range(0, self.m):
                        for j in range(0, self.n):
                                ans.data[i][j] = -self.data[i][j]
                return ans
                
                
        def __mul__(self,B):
                if type(B) is int:
                        ans = matrix(0,self.m,self.n)
                        m = 0
                        for row in self.data:
                                n = 0
                                for val in row:
                                        ans.data[m][n] = val*B
                                        n += 1
                                m += 1
                
                if type(B) is float:
                        ans = matrix(0,self.m,self.n)
                        m = 0
                        for row in self.data:
                                n = 0
                                for val in row:
                                        ans.data[m][n] = val*B
                                        n += 1
                                m += 1
                if type(B) is matrix:
                        ta = size(self)
                        tb = size(B)
                        if ta[1]==tb[0]:
                                ans = matrix(0,ta[0],tb[1])
                                for i in range(0,ta[0]):
                                        for j in range(0,tb[1]):
                                                val = 0
                                                for x in range(0,ta[1]):
                                                        val += self.row(i+1)[x]*B.col(j+1)[x]
                                                
                                                ans.data[i][j] = val
                        else:
                                raise TypeError('Dimensions mismatch')
                return ans
        def __str__(self):
                txt = '[['
                m = -1
                for i in self.data:
                        m += 1
                        n = -1
                        for j in i:
                                n += 1
                                txt+= (str(j))
                                if n<len(self.data[0])-1:
                                        txt += ',\t'
                        if m<len(self.data)-1:
                                txt += '],\n ['
                                n = -1
                txt += ']]'
                return txt
                        
        def act(self):
                self.m = len(self.data)
                self.n = len(self.data[0])
        def __call__(self,i,j):
                return self.data[i-1][j-1]
        
        def dot(self,A):
                ta = size(self)
                tb = size(A)
                print('Arreglar por que no es producto punto')
                if ta[0]==tb[0] and ta[1]==tb[1]:
                        ans = zeros(self.m,self.n)
                        for i in range(0,self.m):
                                for j in range(0,self.n):
                                        ans.data[i][j] = self(i+1,j+1)*A(i+1,j+1)
                return ans
        
        def col(self,n):
                ans = []        
                for x in self.data:
                        ans.append(x[n-1])
                return ans
        def ind(self,vm,vn):
                m = len(vm)
                n = len(vn)
                ans=zeros(m,n)
                for i in range(0,m):
                        for j in range(0,n):
                                ans.data[i][j]=self(vm[i],vn[j])
                return ans
        def row(self,m):                
                ans = self.data[m-1]
                return ans
        def max(self):
                ans = max(self.data)
                return ans
        def min(self):
                ans = min(self.data)
                return ans
        def times(self,A):#Producto elemento a elemento ==> a.*b en matlab
                ta = size(self)
                tb = size(A)
                if ta[0]==tb[0] and ta[1]==tb[1]:
                        ans = zeros(self.m,self.n)
                        for i in range(0,self.m):
                                for j in range(0,self.n):
                                        ans.data[i][j] = self(i+1,j+1)*A(i+1,j+1)
                return ans
                
                
        __radd__ = __add__
        __repr__ = __str__
        size = size
        det = det
        ind = ind
        transpose = transpose
        inv = inv
        
        
        
x = matrix([[1,2,3],[4,5,6],[7,8,9]])

print('matriz inicial\n',x)
print('indice (3,2) = ',x(3,2))

y = matrix([[2],[3],[4]])


print(x*y)
i=0
j=1
a = matrix([[.3,.52,1],[.5,1,1.9],[.1,.3,.5]])
b = matrix([[1,1,3,-2],[2,-4,7,2],[3,-2,9,-1],[1,3,-1,1]])
x=matrix([[1,2],[3,4]])
x
print(inv(x))
