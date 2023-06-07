# taking data from the user, type-casting the data from string to int and storing it in respective variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: ")) 

#display the values before and after swapping
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a # swapping the values of a and b
print(f"After swap: a = {a}, b = {b}")

                        # or
                         
# Optimising the above code into single line instruction
a = int(input("Enter first number: ")); b = int(input("Enter second number: ")) ; print(f"Before swap: a = {a}, b = {b}"); a, b = b, a; print(f"After swap: a = {a}, b = {b}")
