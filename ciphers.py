# Input keyword and message
keyword = input("Keyword (A–Z): ").strip().upper()
# This takes the input from the user for the keyword. It strips any extra spaces and converts it to uppercase.

message = input("Message: ").strip().upper()
# This takes the input for the message, strips any leading/trailing spaces, and converts it to uppercase.

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# This creates a list of uppercase English alphabet letters (A-Z), which we will use later for indexing the letters.

# Keep only letters (remove non-alphabetical characters)
msg = "".join(ch for ch in message if ch.isalpha())
# This filters out any non-alphabetical characters from the message.
# It loops through each character in the message, checks if it is a letter (using `isalpha()`),
# and then joins those valid letters back into an empty string.

# 1) Distribute characters into columns
cols = [[] for _ in range(len(keyword))]
# This creates an empty list of lists (`cols`) to represent the columns.
# The number of columns is equal to the length of the keyword, as each column will correspond to a character in the keyword.

for i, ch in enumerate(msg):
    # This loop iterates over each character in the `msg` (filtered message).
    # `enumerate` gives both the index `i` and the character `ch`.

    cols[i % len(keyword)].append(ch)
    # The character `ch` is added to a column.
    # The column is selected by `i % len(keyword)`, which cycles through columns in a round-robin manner.
    # For example, if `keyword` has 4 letters, it will add characters to columns 0, 1, 2, 3 in order,
    # then start again at column 0.

# 2) Shift each column by its keyword letter



for i, col in enumerate(cols):
    shift = letters.index(keyword[i])
    new_position = [(i + shift) % 26] 
    for n in range(len(col)):
        col[n] = letters[(i + shift) % 26]
        print(col[n])
