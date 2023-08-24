import json

table_replace_json = open('src/table-replace.json')
table_replace_data = json.load(table_replace_json)

with open(r'README.md', 'r') as readme:
    data = readme.read()

    for i in table_replace_data:
        if(i['eval'] is True):
            data = data.replace(i['search'], i['replace'])

with open(r'README.md', 'w') as readme:
    readme.write(data)

table_replace_json.close()