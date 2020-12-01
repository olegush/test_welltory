import os
import json


def check_data(path):
    schemas = dict()
    with os.scandir(path) as entries:
        for entry in entries:
            with open(os.path.join(path, entry.name)) as f:
                schemas[entry.name] = f.read()
    for name, data in schemas.items():
        print(name, json.loads(data))


if __name__ == '__main__':
    check_data('task_folder/schema')
