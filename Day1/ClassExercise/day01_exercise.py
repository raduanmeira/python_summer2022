# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence

count = 0
x = 1
y = 1

while (count < 11):
  count = count +1
  if (count < 3):
    print(x)
  else: 
    x = x + y
    y = x - y
    print(x)
  

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
  length = len(word)
  for i in range(0, length):
    if word[i] == "e":
      print(False)
    
word = "five"
has_no_e("five")
"""return true if there is e in 'word', else false"""
def has_e(word):


"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):


"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):


"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):
