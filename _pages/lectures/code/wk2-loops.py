classcode = "CMSC 140"
if classcode == "CMSC 140":
    print("Welcome to Class!")

classcode = "CMSC 140"
while classcode == "CMSC 140":
    print("Welcome to Class!")
    classcode = "hello"

print(classcode)

num_times = 0
x = 0
while num_times < 5:
    num_times = num_times + 1
    response = "This block has executed " + str(num_times)
    if num_times == 1:
        print(response + " time.")
    else:
        print(response + " times.")
    x += 5
print("Value of num_times variable:", num_times)
print("Value of x variable:", x)


for j in range(1,6):
    response = "This block has executed " + str(j)
    if j == 1:
        print(response + " time.")
    else:
        print(response + " times.")

print("Value of j variable:", j)

print("one args: ")
for i in range(10):
    print(i)

print(" two args: ")
for i in range(4, 10):
    print(i)

print("three args:")
for i in range(10, 4, -1):
    print(i)

# Escpae characters
#print("Here are some escapes: \' \" \\ ")
#print(r"lkghdlkgh20393''''\ ")