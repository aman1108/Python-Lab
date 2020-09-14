class Gen:
    def __init__(self,n):
        self.n=n
    def __iter__(self):
        return self
    def __next__(self):
        if(self.n==0):
            raise StopIteration
        if(self.n%7==0):
            self.n=self.n-1
            return (self.n+1)
        self.n=self.n-1

G= Gen(18)
for i in G:
    print(i)
    
        
