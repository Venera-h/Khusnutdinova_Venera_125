import json

with open('file1.json', 'r') as read_file:
    dict_obj= json.load(read_file)
    print(dict_obj)

#with open("people.json") as f:
 #   data = json.load(f)
