'''
Name: Achintya Kamath
Roll Number: R030
MBA Tech Artificial Intelligence
Subject: Natural Language Processing
Lab 00 - File Handling and Regular Expressions
Date: 20/07/2023
'''

# Info about me and the practical
print("\n ############# ################ ####################\n")

print(" Name: Achintya Kamath \n Roll Number: R030 \n Program: MBA Tech Artificial Intelligence \n Subject: Natural Language Processing \n Lab 00 - File Handling and Regular Expressions \n Date: 20/07/2023")

print("\n ############# ################ ####################")

# importing stuff
from msilib import sequence
import re

#File Handling
#Task A

#First 5 characters
only_five_characters = open("Hello.txt", "r")
print("\n The first 5 characters of the text file 'Hello.txt' are:\n", only_five_characters.read(5))

only_five_characters.close()

#Line by Line
line_by_line = open("Hello.txt", "r")
print("\n Displaying the contents of 'Hello.txt' line by line:\n")

for line in line_by_line:
    print(" ",line, end="")

line_by_line.close()

#All Lines
all_lines = open("Hello.txt", "r")
print("\n\n All lines present in the text file 'Hello' are:\n", all_lines.readlines())

all_lines.close()

#Specific Line
specific_line = open("Hello.txt", "r")
print("\n Displaying the second line from the text file 'Hello':\n", specific_line.readlines()[1])

specific_line.close()

#Task B

#Creating a file then writing in it

print(" Creating and writing a text file:")

i_wrote_this_file = open("test.txt", "x")
i_wrote_this_file.write("Hello World :D\nHello Python :)")
i_wrote_this_file.close()

i_wrote_this_file = open("test.txt", "r")
for line in i_wrote_this_file:
    print(" ", line, end="")
i_wrote_this_file.close()

#Writing a list of fruits in a .txt

print("\n\n Creating a text file containing a list of fruits:")

someones_fruit_list = open("fruits.txt", "x")
someones_fruit_list.write("Apple\n Apricot\n Avocado\n Banana\n Bilberry\n Blackberry\n Blackcurrant\n Blueberry\n Boysenberry\n Currant\n Cherry\n Cherimoya\n Chico fruit\n Cloudberry\n Cranberry\n Custard apple\n Damson\n Date\n Dragonfruit\n Durian\n Elderberry\n Feijoa\n Fig\n Goji berry\n Gooseberry\n Grape\n Raisin\n Grapefruit\n Guava\n Honeyberry\n Huckleberry\n Jabuticaba\n Jackfruit\n Jambul\n Jujube\n Juniper berry\n Kiwano\n Kiwifruit")
someones_fruit_list.close()

someones_fruit_list = open("fruits.txt", "r")
for fruit in someones_fruit_list:
    print("", fruit, end="")
someones_fruit_list.close()

#Task C

#Read Resume

print("\n\n Reading a resume:")
resume_reader = open("Biodata.txt", "r")
for details in resume_reader:
    print(" ", details, end="")
resume_reader.close()

#Regular Expression
#Task A

#Searching Sequence
text = "hello world"
sequence_searcher = re.findall(r"he.....o",text)
print("\n\n Searching for a sequence that starts with 'he' followed by two characters and an 'o':\n", sequence_searcher)

#Task B

#Searching String
spanish_inquistion = "The rain in Spain"
the = re.search(r"\AThe",spanish_inquistion)
spain = re.search(r"Spain\Z",spanish_inquistion)
the_spain = re.search(r"^The Spain$",spanish_inquistion)

print("\n Searching for 'The':", the,"\n Searching for 'Spain':", spain, "\n Searching for 'The Spain':", the_spain)

#Task C

#Finding Lower and Upper Case Characters
upper_spain = re.search('[A-M]+$',spanish_inquistion)
lower_spain = re.search('[a-m]+$',spanish_inquistion)

print("\n Upper Lettered Words:\n ", upper_spain, "\n", lower_spain)

#Task D
#Searching for first whitespace character
print("\n First Whitespace:\n ", (spanish_inquistion.split(" "))[0])

#Task E
#Replacing whitespace with '9'
print("\n Replacing whitespace with '9':\n ", "9".join(spanish_inquistion.split(" ")))

#Task F
#Checking if email ID is vaild

email = input("\n Please enter your email address:")
check = [['gmail',"com"],['yahoo',"co","in"],["hotmail","com"]]
to_be_checked = ((email.split("@"))[1]).split(".")

if to_be_checked in check:
    print("\n Email is Valid.")

else:
    print("\n Email is Invalid.")

