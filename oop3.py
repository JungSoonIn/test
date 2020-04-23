class Set:
    def __init__(self, value = []):    # Constructor
        self.data = []                 # Manages a list
        self.concat(value)

    def intersection(self, other):        # other is any sequence
        res = []                       # self is the subject
        for x in self.data:
            if x in other:             # Pick common items
                res.append(x)
        return Set(res)                # Return a new Set

    def union(self, other):            # other is any sequence
        res = self.data[:]             # Copy of my list
        for x in other:                # Add items in other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):
        for x in value:                
            if not x in self.data:     # Removes duplicates
                self.data.append(x)

    def __len__(self):          return len(self.data)        # len(self)
    def __getitem__(self, key): return self.data[key]        # self[i], self[i:j]
    def __and__(self, other):   return self.intersection(other) # self & other
    def __or__(self, other):    return self.union(other)     # self | other
    def __repr__(self):         return 'Set({})'.format(repr(self.data))  
    def __iter__(self):         return iter(self.data)       # for x in self:

    def issubset(self, other) :
        inter = 0
        for i in self.data :
            if i in other.data :
                inter += 1
        if inter == len(self.data) :
            return True
        else :
            return False
       
    def issuperset(self, other) :
        inter = 0
        for i in other.data :
            if i in self.data :
                inter += 1
        if len(self.data) >= len(other.data) and inter == len(other.data) :
            return True
        else :
            return False

    def intersection_update(self, *others) :
        a = self.data
        for i in others :
            for j in a :
                if j not in i :
                    a.remove(j)
        self = Set(a)
        return self                

    def difference_update(self, *others) :
        a = self.data
        for i in others :
            for j in i :    
                if j in a :                # 위와 같은 실수함 (others 안의 i를 리스트 안의 요소라고 생각함)
                    a.remove(j)
        self = Set(a)
        return self

    def symmetric_difference_update(self, other) :
        a = self.data
        b = other.data
        c = a + b
        d = Set(c)
        for i in a :
            if i in b :
                d.remove(i)
        self = d
        return self

    def add(self, elem) :
        if elem not in self.data :
            self.data.append(elem)
    
    def remove(self, elem) :
        try :
            if elem in self.data :
                self.data.remove(elem)
            else :
                raise KeyError
        except KeyError :
            print("There is no {0} in current set".format(elem))
    
    def __lt__(self, other) :
        if self.data != other.data and self.issubset(other) :
            return True
        else :
            return False

    def __le__(self, other) :
        if self.issubset(other) == True :
            return True
        else :
            return False

    def __gt__(self, other) :
        if self.data != other.data and self.issuperset(other) :
            return True
        else :
            return False

    def __ge__(self, other) :
        if self.issuperset(other) == True :
            return True
        else :
            return False

    def __ior__(self, other) :
        for i in other.data :
            if i not in self.data :
                self.data.append(i)
        return self

    def __iand__(self, other) :
        self = self.intersection_update(other)
        return self


    def __isub__(self, other) :
        a = self.data
        for i in other.data :
            if i in a :
                a.remove(i)
        self = Set(a)
        return self


    def __ixor__(self, other) :
        a = self.symmetric_difference_update(other)
        self = Set(a)
        return self



A = Set([1,3,5])
B = Set([2,3,4])
A^=B
print(A)

C = Set([1,2,3])
D = Set([3,4,5])
C&=D
print(C)

E = Set([1,2,3])
F = Set([4,5,6,7])
E|=F
print(E)

G = Set([1,2,3,4])
H = Set([3,4,5,6])
G-=H
print(G)

a = Set([1,2,3,4])
b = Set([1,2])  
print(a>=b)
print(a>b)
print(b<a)

#issubset
print(b.issubset(a))

#issuperset
print(b.issuperset(a))
print(a.issuperset(b))

aa = Set([1,2,3])
bb = Set([1,2,3])
print(aa>bb)
print(aa<bb)
print(aa.issubset(bb))
print(bb.issubset(aa))

x = Set([1,2,3,3,4])
y = Set([2,1,4,5,6])
z = Set([4,5,6,7,8])
print(x, y, z, len(x))

#intersection_update
print(x.intersection_update(y,z))
print(x, y, z, len(x))

#difference_update
d = Set([5,6,7,9])
e = Set([3,5,7,8,6])
f = Set([2,4,6,8])
print(d, e, f, len(d))
print(d.difference_update(e,f))
print(d, e, f, len(x))

#symmetric_difference_update(other)
my = Set([1,2,5,6])
your = Set([1,2,5,7])
print(my.symmetric_difference_update(your))
print(my)

#add(elem)
my1 = Set([1,2,3])
my1.add(4)
my1.add(10)
print(my1)

#remove(elem)remove(elem)
my2 = Set([1,2,3,4,5,10])
my2.remove(1)
my2.remove(11)
print(my2)
