import os
import mybase
import time
# Get the current working directory
current_directory = os.getcwd() + "/files"

print("current_directory: "+ current_directory)

# Iterate through the files in the current directory
for file_name in os.listdir(current_directory):
    # Check if the file has a .csv extension
    if file_name.endswith(".csv"):
        #print("~~~~~~~~~~~~~~~~~~")
        #print(file_name)
        mybase.process_similarity(current_directory+"/"+file_name, 'golden-data.txt')
        time.sleep(1)

