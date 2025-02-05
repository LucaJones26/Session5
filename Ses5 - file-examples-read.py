fp = open("text.txt", "r") # r is by default (not really needed)
print(fp.read()) # prints entire content of the file
fp.close() # good practice to close the file, can't do anymore actions to it


