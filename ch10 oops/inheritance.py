# Single inheritance 

class A:
    def displayA(self):
        print("wlcm to noida")
class B:
# class B(A):
    def displayB(self):
        print("wlcm to delhi")

# Multiple inheritance
class C(A,B):
    def displayC(self):
        print("WLCM to Gurgaon")
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()



