numBottles = 13
numExchange = numBottles / 3
output = numBottles + numExchange + 1

print(output)
maxbottles = 0
fullbottlesback = 0
for i in range(numBottles):
    if i % 3 == 0:
        fullbottlesback += 1



