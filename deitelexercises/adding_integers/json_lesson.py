import json
import yaml

#
# config_dict = {"name":"Adeola", "age": 18, 1: "Birthday", "hobby":[1,2,3,4], "bool": True}
# with open("config.json", mode='w') as file_obj:
#     json.dump(config_dict, file_obj, indent= 4, separators=(',',':'))


with open("config.json",mode="r") as file_obj:
    con = json.load(file_obj)
    print(con)