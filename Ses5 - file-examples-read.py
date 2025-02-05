fp = open("text.txt", "r") # r is by default (not really needed)
print(fp.read()) # prints entire content of the file
fp.close() # good practice to close the file, can't do anymore actions to it

# same thing with context manager this time
with open("text.txt", "r") as fp:
    print(fp.read())

# lets read from the same file line by line
print("Read the file line by line")
with open("text.txt", "r") as fp:
    for line in fp: # we iterate over the file line by line
        print(line, end="") # ask print not to add the new line
        print(line.rstrip())
        pass  # A way to pass through this line without saying anything
print("done printing") # if put end='' then doesnt say
print("done with the code")


#example 3

# lets read from the same file line by line
print("Read the file line by line")
line_number = 1
with open("text.txt", "r") as fp:
    for line in fp: # we iterate over the file line by line
        print(f"{line_number}:{line}", end="")
        line_number += 1
print("done printing")
# make sure to align properly


#example 4 - Now write to a file


