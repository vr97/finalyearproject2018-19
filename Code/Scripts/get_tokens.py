import json

file_path = "D:\\Users\\yashk\\Campaign-Assistant\\tokens.txt"
with open(file_path) as file:
    file_data = json.load(file)

creds = file_data
