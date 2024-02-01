import json

file_prefix = "/Users/sks/seeeds/python/file_io/"
input_file_name = file_prefix + "input.json"
output_file_name = file_prefix + "output.json"

input_file = open(input_file_name)
person_list_object = json.load(input_file)

for person_object in person_list_object:
  current_salary = person_object["salary"]
  new_salary = current_salary + current_salary * 0.2
  print(f'name: {person_object["name"]}') 
  print(f'current salary: {current_salary}')
  print(f'new salary: {new_salary}')
  print('\n ')
  # set the new salary in the object
  person_object["salary"] = new_salary

output_json = json.dumps(person_list_object, indent=2)
print("Updated person list:")
print(output_json)

output_file = open(output_file_name, "w")
output_file.write(output_json)

