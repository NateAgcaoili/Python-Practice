### Dictionary Basics ###
my_dict = {"a":1, "b":2, "c":3}

if "a" in my_dict:
    print(my_dict["a"])

my_dict.get("a") #returns 1

my_dict["d"] = 4 #adds d to dictionary

for k in my_dict: #prints all the keys
    print(k)

for k, elem in my_dict.items():
    print(k,elem) #prints keys values of dictionary

### Hash Table ###
vowels = {"a":0, "e":0, "i":0, "o":0, "u":0}
sentence = "Hello, I went to the store to pick up some pickles but they were out of pickles so I purchased some bananas."

data = sentence.split()

for word in data: #iterates through each word of sentence
    for letter in word: #iterates for each letter in each word
        if letter in vowels: #checks if the letter is in the vowels dictionary
            vowels[letter] += 1 #adds one to key value of the vowel

print(vowels)