import json

with open("subject_details.json",'r') as file:
    json_data = json.load(file)

for key in json_data:
    print(key,"=",json_data[key])


#Value inside json file
""""
{
    "Hindi" : 78,
    "English" : 99,
    "Mathematics" : 88,
    "Science" : 90,
    "Marathi" : 34
}

"""