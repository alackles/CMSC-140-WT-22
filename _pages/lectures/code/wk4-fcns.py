def hello():
    print("Howdy!")
    print("Howdy!!!")
    print("Hello there.")

def hello_three():
    for i in range(3):
        hello()

#hello()
#print("---Sep---")
#hello_three()

def excite(my_string):
    print(my_string + "!!!!!!")

excite("Hello")

def dashes(a, b):
    a = str(a)
    b = str(b)
    print(a + "-" + b)

dashes("one", "two")
dashes(1,2)

q = "Q"
excite(q)

def print_time(hour, minute):
    example = 0
    print(str(hour) + ":" + str(minute))
    print("print_time i", example)

example_num = 20    
hour = 11
minute = 59
print_time(hour, minute)
print("global i", example_num)