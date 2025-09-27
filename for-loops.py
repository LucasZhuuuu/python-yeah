# for number in range (1, 11):
#     print(number)

# divisor = int(input("Please enter a divisor you want to use: "))
# for number in range (1, 11):
#     print("in loop, number = " + str(number))
#     if number % divisor == 0:
#         break

# print("The first number divisible by " + str(divisor) + " is " + str(number) + ".")

# num = int(input("Please find a number to check for prime: "))
# for x in range(2, num):
#     if num % x == 0:
#         print(str(num) + " is not a prime number")
#         break # will  not go to else afterwards
# else:
#     print(str(num) + " is a prime number")

for i in range(20, 1, -1): # searches each number in the range from 20 to 1
    if i % 2 == 0: # if the number modulum 2 is = to 0
        print(i) # print that number.



