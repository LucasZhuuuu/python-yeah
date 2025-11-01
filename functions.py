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



# class calculator:
#     numbers = list[int]
    
#     def numbers_calc(self, num : int):
#         self.numbers.append(num) # this function is for adding the numbers that the user inputed to the list

#     def add(self) -> int: # add is a function, when we do this function we add up the numbers in the list
#         result = 0
#         for num in self.numbers:
#             result += num
#         return result
    
#     def sub(self) -> int: # sub is also a function, this function must start with a number so we take the number at index 0 
#         result = self.numbers[0] # start subtracting from the first number in the self.numbers list
#         for num in self.numbers:
#             result -= num
#         return result
#     print("Give me as many numbers as you want, after, type end")
#     int(input())


    
# def greet(name : str) -> str:
#     print(f"Greetings {name}!")
#     return f"Name is {name}" 

# greet("Lucas")

# def c_to_f(celsius : int) -> int: # c to f is a function that we have defined. Celsius would be inputed as an integer
#     fahrenheit = (celsius * (9/5)) + 32 # what we want the function to do
#     print (fahrenheit) # print the result

# c_to_f(100) # sets what the input is

# def f_to_c(fahr : int) -> int:
#     result =  (fahr - 32)/(5*9)
#     print(result)

# f_to_c(32)

# import random   

# verb = ["jump on a pogo stick", "macarena", "fly", "breakdance", "drive their RAM 1500", "leap", "chase after kids", "set fire"]
# place = ["park", "mall", "cemetary", "restaurant", "coffee shop", "CN tower", "daycare"]


# def story_gen(noun: str):
#     print(f"{noun}, wants to {random.choice(verb)} to the {random.choice(place)}!")
#     print(f"Then, {noun} wants to {random.choice(verb)} to the {random.choice(place)}, yayy!")
    
# print("What do you want your main character's name to be?")

# noun = str(input())

# story_gen(noun)

import random

magicians = ["Grandma", "Bob", "Adam"]
spells = ["Fireball", "Shadow Pull", "Water splash"]

def magician_spell(noun : str):
    print(f"{random.choice(magicians)} casts {random.choice(spells)}")

magician_spell("noun")

print("Who do you want your magician to be?")

magician = input()

if magician == "Grandma":
    print(f"{magician} casts Fireball")

    




