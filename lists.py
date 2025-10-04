m = [1, 2+5, 3, 4, "apple"]
print(m)

list7 = [9, 8, 7, 6, 5]
list7[0] = 10 # replaces the position of the number to 10
print(list7) 


list7.append(1) # adds to the end
list7.insert(0,99) # (place, number value)
print(list7)

del list7[0] # deletes the first position of the list
last = list7.pop(2) # removes the last number that you added, (position)
print(list7)

list1 = []
for i in range(31): # from 0 to 30
    if i % 3 == 0: # checks if the number is divisible by 3, if so 
        list1.append(i) # it adds it to the "list1"
print(list1) # prints list 1 after the for loops is finished.
