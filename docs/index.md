Kevin Bangen

12/05/2020

Foundations of Programming: Python

Assignment 07

# Pickling and Error Handling

## Introduction

This paper will discuss the steps taken in completing Assignment 07. Assignment 07 was more open ended than previous assignments. Assignment 07 required independent research on the topics of pickling and error handling. Script files were then developed to demonstrate pickling and error handling. 

## Independent Research

Like most things Python, a basic Google search revealed lots of articles/tutorials explaining both pickling and error handling. These articles helped to build upon the previous resources that had been provided as part of the class. 
One page that I would like to highlight on the topic of pickling is linked here: https://www.datacamp.com/community/tutorials/pickle-python-tutorial. I liked this article/page because it discussed when NOT to pickle and discussed what kind of data/objects can be pickled.

## Pickling Demo

I created my pickling demo by building on the Lab 7-1 starter. The demo is very simple. It takes data (first and last name) from the user, displays the inputs back to the user, writes the data to a file, and reads the data back from the file. The script is shown here:

```
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
first_name = ""
last_name = ""
full_name=[]

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    file_name = open(file_name, "ab")
    pickle.dump(list_of_data, file_name)
    file_name.close()

def read_data_from_file(file_name):
    file_name = open(file_name, "rb")
    file_data = pickle.load(file_name)
    file_name.close()
    return file_data

# Presentation ------------------------------------ #
first_name = str(input("Enter First Name:"))
last_name = str(input("Enter Last Name:"))
full_name = [first_name, last_name]
print(full_name)
save_data_to_file(strFileName, full_name)
print(read_data_from_file(strFileName))
```

There are a couple of things that I would like to note. This demo will only work successfully for one full name. It does not work properly with multiple names. This demo script is also a little more complex than it needs to be in that it uses functions and feeds into those functions. As I understand it, the script did not need to use functions in this way.

## Error Handling Demo

I created my error handling demo by barrowing script from Assignment02. Assignment02 asked the class to gather numerical inputs from the user and complete some basic mathematical tasks (add, subtract, divide, multiply). If a non-numerical input was provided an error message would appear. The demo includes only the addition task and provides a simple error message if certain inputs, such as letters, are provided. Demo script provided here:
```
strfirstnumber=input("Enter a first number: ") #collects first number from user
strsecondnumber=input("Enter a second number: ") #collects second number from user
try:
    fltfirstnumber=float(strfirstnumber) #converts first number to floating data type
    fltsecondnumber=float(strsecondnumber) #converts second number to floating data type
    print("The sum of",fltfirstnumber,"and",fltsecondnumber,"is",end=": ") #displays text explaining mathmatical operation to be performed
    print(fltfirstnumber+fltsecondnumber) #adds inputs
except:
    print("Cannot process provided inputs!")
print("") #creates blank line
print("Press enter to exit!")
input()
```
## Conclusion

In summary, this paper discussed the steps taken in completing Assignment 07. Assignment 07 was more open ended than previous assignments. Assignment 07 required independent research on the topics of pickling and error handling. Script files were then developed to demonstrate pickling and error handling. 


