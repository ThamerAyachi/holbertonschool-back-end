#!/usr/bin/python3
"""Using API and export it in json file"""

from sys import argv
import json
import requests

url_base = 'https://jsonplaceholder.typicode.com/users/'


def export_json_file(id):
    """Export data to file as json format"""

    file_name = id + ".json"
    user = requests.get(url_base + id).json()
    todo_list = requests.get(url_base + id + '/todos/').json()
    items_data = []
    data_json = dict()

    for task in todo_list:
        item = dict()
        item['task'] = task['title']
        item['completed'] = task['completed']
        item['username'] = user['username']
        items_data.append(item)

    data_json[id] = items_data

    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(data_json, f)


if __name__ == "__main__":
    export_json_file(argv[1])
