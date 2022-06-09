class Main:
    def __init__(self,qrs,db):
        self.qrs=qrs
        self.db=db
    def qr_update(self,string):
        (self.qrs).append(string)
    def db_update(self,string):
        (self.db).append(string)
    def display(self):
        print(self.qrs)
        print("********")
        print(self.db)
    def verifyQR(self,str):
        if (str in self.qrs):return True
        else:return False

main=Main([],[])
#main.display()
 