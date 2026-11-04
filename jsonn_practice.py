import json

with open('practice.json', 'r') as file:
    practice = json.load(file)  

for key, value in practice.items():
    print(f" {key} --> {value}")





