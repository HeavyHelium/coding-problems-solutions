import random

n = 1000000 # number of random points
count = 0

for i in range(n):
    x = random.uniform(-1, 1) # generate a random x-coordinate between -1 and 1
    y = random.uniform(-1, 1) # generate a random y-coordinate between -1 and 1
    
    # check if the point is within the circle
    if x**2 + y**2 <= 1:
        count += 1

# compute the estimated value of pi
pi_est = 4 * count / n

print("Estimated value of pi:", pi_est)

