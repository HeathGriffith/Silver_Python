''' Create a script that generates a list of dictionaries about files (name and size)
in the working directory. Then print the list. '''

import os
files_and_sizes = []

for element in os.listdir():
    if os.path.isfile(element):
        size = os.path.getsize(element)
        dictionary = {"name": element, "size": size}
        files_and_sizes.append(dictionary)

print(files_and_sizes)

