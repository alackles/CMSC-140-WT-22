import random
import matplotlib.pyplot as plt

def chicken_walk(n):
    distance = n
    steps = 0
    while distance != 0:
        choice = random.randrange(0, 100)
        #print(choice)
        if choice % 2 == 0: # if even
            distance += 1
        else: # if odd
            distance -= 1
        steps += 1
    return steps 

inputs = [] 
distances = []

for _ in range(0):
    input_number = random.randint(1, 10)
    dist = chicken_walk(input_number)
    if dist < 150:
        inputs.append(input_number)
        distances.append(dist)

print(inputs)
print(distances)
#plt.scatter(inputs, distances)
#plt.show()

avg_distance = []
for _ in range(100):
    avg_distance.append(chicken_walk(5))
print(sum(avg_distance)/len(avg_distance))