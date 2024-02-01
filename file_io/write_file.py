
file_name = "/Users/sks/seeeds/python/file_io/demowrite.txt"
f = open(file_name, "a")
f.write("This is a test file with some text!\n")
f.close()

#open and read the file after the writing:
f = open(file_name, "r")
print(f.read())