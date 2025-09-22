class parent:
    def method1(self):
        print("this is parent class")

class child:
    def method2(self):
        print("this is child class")

class child2(parent,child):
    def method3(self):
        print("this is child2 class")

obj=child2()
obj.method3()
obj.method2()
obj.method1()
