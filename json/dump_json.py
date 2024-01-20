import json

# Person list:
person_list_json =  """
[
  {
    "name": "Murugan",
    "salary": 50000,
    "vehicles": [ "bicycle", "motorbike", "car" ]
  },
  {
    "name": "Ganesh",
    "salary": 45000,
    "vehicles": [ "motorbike", "car" ]
  },
  {
    "name": "Siva",
    "salary": 22000,
    "vehicles": [ "car" ]
  },
  {
    "name": "Kannan",
    "salary": 19000,
    "vehicles": [ ]
  }
]
"""

# parse the above json, it becomes a python list:
person_list_object = json.loads(person_list_json)

for person_object in person_list_object:
  current_salary = person_object["salary"]
  new_salary = current_salary + current_salary * 0.2
  print(f'name: {person_object["name"]}') 
  print(f'current salary: {current_salary}')
  print(f'new salary: {new_salary}')
  print('\n ')
  # set the new salary in the object
  person_object["salary"] = new_salary

print("Updated person list:")
print(json.dumps(person_list_object, indent=2))
