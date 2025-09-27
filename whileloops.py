counter = 1
while counter < 5:
    print(counter)
    counter += 1 # shortcut for saying counter = counter + 1

first_name = "Lucas"
last_name = "Zhu"

full_name = first_name + " " + last_name
print(full_name)

power = 0
num = 0
while True:
    digit = int(input('Please enter an integer as a digit'))
    if digit != -1:
        num += digit * (10 ** power)
        power += 1
    else:
        break 
    print(num)