# class Dog: # class is a blueprint template that is used to create an object
#     # attributes
#     # variable_name : variable_type, defining what type of response the attribute should be
#     name: str
#     age: int
#     weight: float
#     favourite_food: str

#     # initializer: special type of function that creates the object ,, you can have multiple initializers, whichever fits
#     def __init__(self, _name, _age, _favourite_food): # relates to the attributes
#         self.name = _name
#         self.age = _age
#         self.favourite_food = _favourite_food
#         self.weight = 10.3

#     def eat(self, food: str) -> float: # function header
#         print(f"{self.name} ate {food}! He enjoyed it very much!") # this statement has an f so it can take varaiables and strings
#         self.weight += len(food) # this is just an example, so for now we just did "add the amount of letters in the food to the total weight"
#         print(f"{self.name} is now {self.weight} kg. What a fat dog!")

# billy_bob = Dog("billy bob", 3, "steak") # this defines what the output is, whatever the name or food 

# billy_bob.eat("steak")



class calculator:
    numbers = list[int]
    
    def numbers_calc(self, num : int):
        self.numbers.append(num) # this function is for adding the numbers that the user inputed to the list

    def add(self) -> int: # add is a function, when we do this function we add up the numbers in the list
        result = 0
        for num in self.numbers:
            result += num
        return result
    
    def sub(self) -> int: # sub is also a function, this function must start with a number so we take the number at index 0 
        result = self.numbers[0] # start subtracting from the first number in the self.numbers list
        for num in self.numbers:
            result -= num
        return result
    print("Give me as many numbers as you want, after, type end")
    int(input())


    


