import os

# Specify the path of the directory you want to list
# If no path is provided, it lists the contents of the current working directory
directory_path = "/"  # current directory

# List the contents of the directory
directory_contents = os.listdir(directory_path)

# Print the contents of the directory
print(directory_contents)