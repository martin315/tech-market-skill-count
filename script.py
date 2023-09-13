import json
import os

f = open("data/SampleData_01.json", "r")
data_path = ".//data"
dir_list = os.listdir(data_path)

data = json.load(f)

for i in data:
    print(i["description"])

print(dir_list)

f.close()