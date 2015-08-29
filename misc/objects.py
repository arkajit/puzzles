import json

REF = "$ref"

# graph = list({})
def expand(graph):
  # id -> object
  objects = {}
  root = graph[0]['id']
  for o in graph:
    objects[o['id']] = o
  return resolve(objects, root)

# objects: id -> {}
def resolve(objects, identifier):
  obj = objects[identifier] 
  if REF not in obj:
    return obj
  else:
    for refId in obj[REF]:
      obj[refId] = resolve(objects, refId)
    del obj[REF]
    return obj

graph = [
  {'id': 'student1', 'name': 'student1', REF: ['school1']},
  {'id': 'school1', 'name': 'school1', REF: ['staff1', 'staff2']},
  {'id': 'staff1', 'name': 'staff1'},
  {'id': 'staff2', 'name': 'staff2'}
]

print json.dumps(expand(graph))

