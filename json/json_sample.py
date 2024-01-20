import json

# Single person:
person_json =  """
{
  "name": "Murugan",
  "salary": 50000,
  "vehicles": [ "bicycle", "motorbike", "car" ]
}
"""

# parse the above json, it becomes a python dictionary:
person_object = json.loads(person_json)

# the result is a Python dictionary:
print(f'name: {person_object["name"]}') 
print(f'salary: {person_object["salary"]}')

vehicles_list = person_object["vehicles"]
print(f'number of vehicles: {len(vehicles_list)}')
print(f'vehicle list: {vehicles_list}')

