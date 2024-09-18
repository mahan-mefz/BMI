class mbi :
    def mbi1 (self) :
        self.vazn = int(input("vazn ra vared konid : "))
        self.gad = int(input("gad ra vared konid : "))
        self.mbimetr()

    def mbimetr(self) :
        self.metr = self.gad /100
        print(self.metr)
        
                
class mbismart(mbi) :
    def smart (self):
        self.vaznee = mbi.vazn
        self.gadd = mbi.metr
        print(self.gadd)
        self.gadd = self.gadd ** 2
        print(self.gadd)
        self.enf = self.vaznee / self.gadd
        print(self.enf)

mbi = mbi()
mbismart = mbismart()
while True :
    mbi.mbi1()
    mbismart.smart()