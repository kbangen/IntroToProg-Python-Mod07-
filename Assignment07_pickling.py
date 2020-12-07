# ------------------------------------------------- #
# Title: Assignment07 Pickling Demo
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# Kevin Bangen, 12/5/2020, Updated processing and title
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
