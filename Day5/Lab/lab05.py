import re
import os
# open text file of 2008 NH primary Obama speech
os.chdir("C:\\Users\\radua\\onedrive\\washu\\classes\\python_course\\python_summer2022\\Day5\\lab")
with open("obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

re.findall(r"the", obama)

re.findall(r'the', obama, re.MULTILINE)

the_drop = re.compile(r"the")

for i, line in enumerate(obama):
    if not the_drop.search(line):
        print(i)
        print(line)

# TODO: print lines that contain a word of any length starting with s and ending with e

s_e_word = re.compile(r"^s\w*")

for i, line in enumerate(obama):
    if s_e_word.search(line):
        print(i)
        print(line)


## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'





