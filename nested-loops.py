# for i in range(0, 101, 5):
#     print(i)

# m = int(input("Enter m: ")) # input m as an integer
# n = int(input("Enter n: ")) # 
# counter = 0 #
# for i in range (m):
#     for j in range (n):
#         counter += 1
#         print("i: ", i, "j: ", j)
# print("The inner loop executed", counter, "times")


# m = 3 # what the variable starts at
# n = 1
# for i in range(3):# number of rows
#     for j in range(m): # since m = 3, when the loop runs the first time, it prints 3 spaces.
#         print(" ", end= " ")
#     for k in range(n):# number of columns
#         print("*", end= " ")
#     print() # seperates the stars by row
#     n += 2 # adds 2 stars after each row
#     m -= 1 # removes a space after each row for the stars
    






# numSpaces = 0 # starts at 0
# column = 7
# for i in range(4):
#     for k in range(numSpaces):
#         print(" ", end= " ") # keeps it in the same row
#     for j in range(column):
#         print("*", end= " ")
#     print() # moves on to the next row.
#     column -= 2
#     numSpaces += 1


for i in range(1, 11): # every 1 i goes, j (1, 2, 3, 4 ...10) multlipies by the value of i. If i = 2, then j (1, 2...10) will multiply by 2.
    for j in range(1, 11):
        print (i * j, end= " ") # prints the value of i times that row of j
    print() # goes to the next row
      



