import os

# print the current directory
print("The current directory:", os.getcwd())

# changing the current directory to 'Python_OS_Files'
os.chdir("Python_OS_Files")

# printing the current directory now
print("The current directory changing the directory to folder:", os.getcwd())

# make an empty directory (folder)
    # os.mkdir("folder")

# running mkdir again with the same name raises FileExistsError, run this instead:
if not os.path.isdir("folder"):
     os.mkdir("folder")

# changing the current directory to 'folder'
os.chdir("folder")

# go back a directory
    # os.chdir("..")

# make several nested directories
os.makedirs("nested1/nested1.2/nested1.3","nested2")

