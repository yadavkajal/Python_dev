import json

with open("subject_details.json","r") as file:
    json_data=json.load(file)
print("Sub | Sem | Marks | Pass")
def func(json_data):
    for key in json_data:
        print(key, "|",json_data[key].get("semester"),"|",json_data[key].get("marks"),"|",json_data[key].get("isPass"))
func(json_data)