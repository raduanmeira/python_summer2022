## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script and see your results.

def count_vowels(word):
  if type(word) != str:
    print("Make sure to type a word!")
    return None
  else:
    count = 0
    for i in range(0, len(word)):
      letter = word.lower()[i]
      if letter in ["a", "e",  "i ", "o", "u"]:
        count = count + 1
    return count    
    
word = 10  
count_vowels(word)

word = "WORD"
count_vowels(word)
