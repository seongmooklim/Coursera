# Question 2
# The new_directory function creates a new directory inside the current working directory, 
# then creates a new empty file inside the new directory, and returns the list of files in that directory. 
# Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 

import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if not os.path.isdir(directory):
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'a+') as file:
    file.write("Hello World")
  # Return the list of files in the new directory
  return os.listdir(directory)

print(new_directory("PythonPrograms", "script.py"))
