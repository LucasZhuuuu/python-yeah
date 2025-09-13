# code tells user what to wear depending on the weather
print("hello there! I'm the weather program, i'm going to help you what to wear today" \
      "Describe what it's like"
)

description = input().split()

clothing = [] # empty list

# for loop = each element performs
for word in description:
    if word == "cold":
        clothing.append("long sleeve") # dot = go one level deeper
    elif "rain" in word:
        clothing.append("rain jacket")
    elif "cloud" in word:
        clothing.append("jeans")
    elif word == "hot":
        clothing.append("t-shirt")

print(clothing)

print("Based off of your description, you should wear: ")

for clothing_item in clothing:
    if clothing_item[len(clothing_item) - 1] == "s":
        print(f"a pair of {clothing_item}")
    else:
        print(clothing_item)
    