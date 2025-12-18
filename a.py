a=1
b=1
c="dfdlf"
d = None
# print (a + b)

a =32
t =type(a)  # will return <class 'int'>

# print(t)
# a = input("Enter a number: ") # this will take input in form of string

#strings 
name = "John"

nam = name[0:3]  # slicing the string (it will return 'Joh')

friend = ["Mike", "Sara", "Tom", 5, 6.7, True]  # list of strings and other data types

# dictionary

marks = {
    "John": 90,
    "Mike": 85,
    "Sara": 92,
}
# print(marks["John"])  # will print 90

#set
unique_numbers = {1, 2, 3, 4, 5}

# if-else statement
if(a == 32):
    print("a is 32")
elif(a == 31):
    print("a is 31")
else:
    print("a is not 31 or 32")


# while loop
i = 0
while(i < 5):
    print(i)  # will print numbers from 0 to 4
    i += 1

# for loop
for j in range(0,5,1): # range(start, stop, step)
   # for j in range(5): # range(5) is equivalent to range(0, 5, 1)
    print(j)  # will print numbers from 0 to 4