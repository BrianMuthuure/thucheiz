import json

people_string = '''
{
"people": [
{
  "name":"Brian Muthuure",
  "phone":"0713780714",
  "emails":["brianmuthuure@gmail.com", "thucheiz@gmail.com"],
  "has_license":false
},
{
  "name":"Betty Mukami",
  "phone":"0797237833",
  "emails":null,
  "has_license":true
  }
  ]
  }
'''

# loading into python object

data = json.loads(people_string)
for person in data['people']:
   print(person['name'])
