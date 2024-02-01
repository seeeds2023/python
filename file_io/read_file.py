file = open("/Users/sks/seeeds/python/file_io/demo.txt", "r")

print(file.read())

file.seek(0)

for line in file:
  print(f'{len(line)}: {line}')

# for index, line in enumerate(file):
#   print(f'{index}: {line}')


file.close()