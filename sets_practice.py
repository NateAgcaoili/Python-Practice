### Set Basics ###
items = {"sword", "rubber duck", "slice of pizza"}
items.add("sword") #sets cannot have repeats, will not be added
print(items)

### Practice ###
vowels = {"a", "e", "i", "o", "u"}
sentence = "Hello, I went to the store to pick up some pickles but they were out of pickles so I purchased some bananas."
seen = set()
data = sentence.split()

for word in data:
   for letter in word:
       if letter in vowels:
           seen.add(letter)

print(seen)

### Union and Intersection ###
colors_one = {"red", "black", "green", "gold"}
colors_two = {"blue", "gold", "white", "red"}

all_colors = colors_one | colors_two #union
print(all_colors)

same_colors = colors_one & colors_two #intersection
print(same_colors)