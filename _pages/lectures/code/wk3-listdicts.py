my_list = [1, 3, 4, 5, 8]
print(my_list)

my_mix = [1, 3, "four", 5, True]
print(my_mix)

a = my_list[0]
print(a)

classes = ["CMSC", "MATH", "STAT", "BIOL", "ART", "MUS"]
print(classes[0:4])

print(classes)
#classes[0] = "PHYS"
#print(classes)

classes = classes  + ["PHYS"]
print(classes)
a = str(classes)
print(a + "hello")

## appending 
classes.append("FYS")
print(classes)

## printing and joining
a = "---".join(classes)
print(a)

greeting = "Hello, my name is Acacia!"
g = greeting.split(" ")
no_a = greeting.split("a")
print(g)
print(no_a)

#nums = input("Enter three numbers separated by commas.")
#a, b, c = nums.split(",")
# like saying:
# a = nums[0]
# b = nums[1]
# c = nums[2]
#print(nums.split(","))
#print(a)
#print(b)
#print(c)

my_dict = {
    0: 2,
    "hello": 2939392,
    1.23: "hi"
}

a = my_dict["hello"]
print(a)

student_dict = { 
    "Acacia": 2830084,
    "Kurt": 1919182,
    "Joe": 89483929,
}

student_names = [["Acacia", 2830084], ["Kurt", 1919182]]
name = input("What is your name?")
print("Your ID number is", student_dict[name])


nums = [1, 3, 4, 8]
for index, i in enumerate(nums):
    a = i**2
    print(index, ":", "square of", i, "is", a)

# Iterating over keys in a dictionary


# Iterating over values in a dictionary