
class Animal:
    def __init__(self,nomi:str,turi:str):
        self.nomi = nomi
        self.turi = turi

    def show_info(self):
        print("Nomi: ",self.nomi)

    def show_info2(self):
        print("Turi: ",self.turi)

ob = Animal("Yulbars","Yirtqich")

ob.show_info()
ob.show_info2()
    
        
