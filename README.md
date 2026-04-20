Dillan van Wyk:

20/04/26: Used Google's AI Overview to figure out how to use the 'global' keyword in order to fix a bug where the high score was reset after every session.
SEARCH:
"what does global key mean in python"

RESPONSE:
In Python, the global keyword is a statement used inside a function to indicate that a specific variable belongs to the global scope (the top-level scope of a module). 
It allows you to modify a variable that was defined outside of the function, rather than creating a new local variable with the same name inside the function. 

Core Functions and Purpose
Modifying Global Variables: By default, if you assign a value to a variable inside a function, Python treats it as a local variable. To change a global variable's value from within a function, you must declare it with global.
Preventing Local Shadowing: It tells Python, "Do not create a new local variable; use the one from the module level".
Sharing State: It is used to share and update a variable's state across different functions or modules. 
How to Use global
Without global (Creates a local variable):
python
x = 10
def modify_x():
    x = 20  # This creates a new LOCAL variable x
    print("Inside:", x)

modify_x()
print("Outside:", x)  # The global x remains 10
# Output:
# Inside: 20
# Outside: 10
With global (Modifies the global variable):
python
x = 10
def modify_x():
    global x  # Declares that we are using the global x
    x = 20    # Modifies the global x
    print("Inside:", x)

modify_x()
print("Outside:", x)  # The global x is now 20
# Output:
# Inside: 20
# Outside: 20
Important Rules and Considerations
Access vs. Modification: You can read (access) global variables inside a function without the global keyword, but you cannot reassign (modify) them.
Mutable Objects: If a global variable is a mutable object (like a list or dictionary), you can modify its contents (e.g., list.append()) without the global keyword. You only need global when you want to reassign the variable to a new object (e.g., list = [1, 2]).
Best Practice: Overusing global is discouraged because it can make code harder to debug and understand (spaghetti code). It is better to pass variables to functions and return the updated values.
Placement: The global keyword must be declared before the variable is used inside the function. 

Denlan Molokwu:

Luke Abrahamse:
