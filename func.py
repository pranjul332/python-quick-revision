# Function Definition
def avg():
    a = 50
    b = 10
    average = (a + b) / 2
    print ("The average is:", average)
    
avg() # Function Call

# Function Definition with Parameters
def avg(a,b):
    average = (a + b) / 2
    print ("The average is:", average)
    
avg(5,4)


def avg(a,b=14): # b has a default value of 14 it means if we do not pass b while calling the function it will take 14 as value of b
    average = (a + b) / 2
    return average
    
a = avg(5,14)
print("The average returned is:", a)