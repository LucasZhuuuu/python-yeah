# import random

# list = []


# for i in range(20):
#     list.append(random.randint(1, 50))

# print(list, len(list))

# number =(random.randint(1, 50))
# print(number)

# # if number in list:
# #     print(f"This is the number we are looking for: {number}")
# # else:
# #     print("Your number is not in the list")

# def binary_search(x, y):
#     list.sort()
#     print(f"Here is your new sorted list: {list}")
#     first = 0
#     last = len(list)-1
#     middle = (first+last) // 2

#     while(first <= last):
#         if list[middle] == number:
#             return middle
#         elif list[middle] > number:
#             last = middle - 1
#         elif list[middle] < number:
#             first = middle + 1
#         middle = (first + last) // 2
#     return -1 

# print()


# binary_search(list, number)

v = "hello"
reversed_str = ""
for i in range(len(v)-1, -1, -1):
    reversed_str += v[i]
print(reversed_str)
