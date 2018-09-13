# Open file 01.txt
file = open("01.txt", "r")
#print the file type
file_type = type(file)
print(file_type)
#Read the file and print to console
content = file.read()
print(content)
