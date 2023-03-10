import json
# Здесь я пробовала использовать разные папка, но тоже без результатно
#path = "C:\Users\Home\Downloads\text.json"
path = "C:\\Users\Home\Documents\GitHub\Khusnutdinova_Venera_125\json\json_text.json"
with open(path, 'r') as f:
    dict_obj = json.load(f.read())
    print(dict_obj)

