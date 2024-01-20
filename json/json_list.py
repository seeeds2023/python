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
  print(f'name: {person_object["name"]}') 
  print(f'salary: {person_object["salary"]}')

  vehicles_list = person_object["vehicles"]
  print(f'number of vehicles: {len(vehicles_list)}')
  print(f'vehicle list: {vehicles_list}')
  print('\n ')

