class employee:
    salary = 12300
    language = "hindi"

    def __init__(self, name, language, salary): #dunder method which is automatically called 
        self.name = name
        self.language = language
        self.salary = salary 
        print("I am creating an object")

harry = employee("Harry", "python" , 12000)
print(harry.name, harry.language, harry.salary)    