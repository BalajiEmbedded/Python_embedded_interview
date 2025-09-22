class father:
    def method1(self):
        print('father method')

class mother:
    def method2(self):
        print('mother method')

class son(father,mother):
    def method3(self):
        print('son method')

class other(mother):
    def method4(self):
        print('other method')

obj = son()
obj.method3()
obj.method1()
obj.method2()
obj1=other()
obj1.method4()
obj1.method2()