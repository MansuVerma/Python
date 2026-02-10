class employee:
    name = "Default name"
    company = "ITC"
    def show(self):
        print(f"The name is {self.name} and the he is working with is {self.company}")

class coder:
    language = "Python"
    def printlanguage(self):
        print(f"The famous language loved by everyone is {self.language}")


class Programmer(employee, coder):
    company = "ITC Infotech"
    language = "Java"
    def showlanguage(self):
        print(f"The new company is {self.company} and the language preffered is {self.language}")


a = employee()
b = Programmer()
c = coder()

a.show()
b.show()
b.printlanguage()
b.showlanguage()
c.printlanguage()