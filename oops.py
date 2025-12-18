class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000
    
    def _inti_(self): # dunder method which is called constructor and will be called automatically when an object is created
        print("Good morning")
    
    def getInfo(self):
        print (f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod # static method does not take self as parameter
    def greet():
        print("Good morning")

    def hi(): # this will give error because it does not have self parameter or is not a static method
        print("Good morning")
        
harry = Employee()
# harry.language = "JavaScript" # This is an instance attribute
harry.greet()
harry.getInfo()
harry.hi()
# Employee.getInfo(harry)