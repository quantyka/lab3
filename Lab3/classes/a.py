class StringProcessor:
    def getString(self):
        self.text = input("Введите строку: ")  

    
    def printString(self):
        print(self.text.upper())  

sp = StringProcessor()


sp.getString()    
sp.printString()  