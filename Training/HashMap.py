class HashMap:
    def __init__(self,size,mod=15):
        self.size=size

        self.l=[None for i in range(size)]
        self.mod=mod

    def add(self,value):
        ind=value%self.mod
        while self.l[ind]!=None:
            ind+=1
        self.l[ind]=value

    def find(self,value):
        ind=value%self.mod