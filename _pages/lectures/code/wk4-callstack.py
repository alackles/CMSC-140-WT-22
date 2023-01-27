print("Start of Script.")

def outer_function():
    print("Outer Function Called.")
    inner_function()
    print("Outer Function Ends.")

def inner_function():
    print("Inner Function Called.")
    print("Inner Function Ends.")

outer_function()

print("End of Script.")
