# for row in range(5):
#     for col in range(5):
#         if row % 2 != 0:
#             print("O", end= " ")
#         else:
#             print("X", end= " ")
#     print()

# for row in range(1, 6):
#     for col in range(1, 6):
#         print(row * col, end= " ")
#     print()


for row in range(5, 0, -1):
    for col in range(row):
        print("*", end = " ")
    print()
    