# note: variables allow you to store some kind of value
# ex: speed = 3.14159
print ('hello, what is your name?')
name = input () # allowing users to type in something

print(f'nice to meet you {name}!')
print('what year were you born in?')

year = int(input())
age = 2025 - year

print(f'wait, {name} has your birthday passed yet?')
y_or_n = input()

if 'n' in y_or_n:
    age = age - 1

print(f"I've got it! {name} you are {age} years old!")

