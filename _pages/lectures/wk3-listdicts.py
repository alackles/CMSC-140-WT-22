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

classes = [classes , ["PHYS"]]
print(classes)
a = str(classes)
print(a + "hello")

my_dict = {
    0: 2,
    "hello": 2939392,
    1.23: "hi"
}

a = my_dict["hello"]
print(a)

nums = [1, 3, 4, 8]
for index, i in enumerate(nums):
    a = i**2
    print(index, ":", "square of", i, "is", a)