# m = [1, 2+5, 3, 4, "apple"]
# print(m)

# list7 = [9, 8, 7, 6, 5]
# list7[0] = 10 # replaces the position of the number to 10
# print(list7) 


# list7.append(1) # adds to the end
# list7.insert(0,99) # (place, number value)
# print(list7)

# del list7[0] # deletes the first position of the list
# last = list7.pop(2) # removes the last number that you added, (position)
# print(list7)

# list1 = []
# for i in range(31): # from 0 to 30
#     if i % 3 == 0: # checks if the number is divisible by 3, if so 
#         list1.append(i) # it adds it to the "list1"
# print(list1) # prints list 1 after the for loops is finished.

# lst = [1, 3, 5, 7, 9, 11]

# last_index = len(lst) - 1
# lst[-1] == lst[last_index]

# for i in range(last_index, -1, -1):
#     print(lst[i])

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# for index in range(len(l1)): # every element in l1
#     l1.insert(index +1, l2[index]) # inserts the index of l2 into l1, but after each one in l1
# print(l1)

# lst = [3, 0, 1]

# lst.sort()
# lst.insert(2,2)
# print(lst)

lst = [8, 5, 6, 2, 7, 9, 4, 1] # defines the list

lst.sort() # sorts list from smallest to biggest

correct_lst = [] # 'correct lst' is set as an empty list
for i in range(min(lst), max(lst)): # for each element from the minimum of lst to the maximum of lst,
    correct_lst.append(i) # add that element to the list 'correct lst'

for num in correct_lst: # for each num in 'correct lst', if that number is not in the original list, then we print that number.
    if num not in lst:# ex. we added each number into 'correct lst' from 1 to 9 since thats the range in 'lst', and the number that wasnt included was 3.
        print(num) # 3 was in 'correct lst' but not in the orignal 'lst' so we print 3.





