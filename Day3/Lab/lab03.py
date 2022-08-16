## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
  if type(txt) != str:
    print("Make sure to type a word!")
  return txt.upper()

## reverse all characters in string
def reverse(txt):
  if type(txt) != str:
    print("Make sure to type a word!")
  else:
    reverse_txt = []
    for i in range(0, len(txt)):
      j =  (len(txt)-1) - i
      reverse_txt += [txt[j]]
  reverse_txt = " ".join([str(item) for item in reverse_txt])
  return reverse_txt

reverse("abcd ef")

## reverse word order in string

def reversewords(txt):
  if type(txt) != str:
    print("Make sure to type a word!")
  else:
    reverse_txt = []
    txt = str.split(txt)
    for i in range(0, len(txt)):
      j =  (len(txt)-1) - i
      reverse_txt += [txt[j]]
  reverse_txt = " ".join([str(item) for item in reverse_txt])
  return reverse_txt

reversewords("ab cdef")

## reverses letters in each word

def reversewordletters(txt):
  if type(txt) != str:
    print("Make sure to type a word!")
  else:
    reverse_txt = []
    reverse_final = []
    txt = str.split(txt)
    for i in range(0, len(txt)):
      a =  (len(txt)-1) - i
      reverse_txt += [txt[a]]
    for j in range(0, len(reverse_txt)):
      b =  (len(reverse_txt)-1) - j
      txt = reverse_txt[b]
      for k in range(0, len(txt)):
        c =  (len(txt)-1) - k
        reverse_final += [txt[c]]
        if k == (len(txt)-1) and j != (len(reverse_txt)-1) : reverse_final += ' '
  reverse_final = "".join([str(item) for item in reverse_final])
  return reverse_final

reversewordletters("ab cd ef")
## optional -- change text to piglatin.. google it!
def piglatin(txt):
  if type(txt) != str:
    print("Make sure to type a word!")
  else:
    phrase = str.split(test)
    for i in range(0, len(phrase)):
      word = phrase[i]
      pig = []
      if word.lower()[0] in ["a", "e", "i", "o", "u"]:
        pig += word+"yay "
      else:
        for j in range(0, len(word)):
          if word.lower()[j] not in ["a", "e", "i", "o", "u"]:
            print(word.lower()[j])
          pigChange[-1] = pigChange[j]
      pig += pigChange+" "
    pig = "".join([str(item) for item in reverse_final])
    return pig


piglatin("Hello there general Kenobi")
## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]


		
			
			
			
			
			
			

