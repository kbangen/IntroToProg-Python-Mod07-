#-------------------------
# Title: Assignment 07 Error Handling Demo
# Dev: Kevin Bangen
# Date: 12/05/2020
# Change Log: (Who, When ,What)
# K Bangen, 12/05/2020, Constructed Demo
#-------------------------

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
