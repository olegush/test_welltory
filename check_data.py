import os
import json
import jsonschema
from jsonschema import validate, Draft3Validator


def check_data(path_schema, path_event):
    schemas = []
    with os.scandir(path_schema) as entries:
        for entry in entries:
            with open(os.path.join(path_schema, entry.name)) as file:
                schema = json.load(file)
                schemas.append(dict(schema_file=entry.name, schema=schema))

    log = []
    for schema in schemas:
        with os.scandir(path_event) as entries:
            for entry in entries:
                with open(os.path.join(path_event, entry.name)) as f:
                    data = json.load(f)
                    try:
                        Draft3Validator(schema['schema']).validate(data)
                    except jsonschema.exceptions.ValidationError as err:
                        log.append(dict(file=entry.name, schema_file=schema['schema_file'], err=err))
    for l in log:
        print(l)


if __name__ == '__main__':
    check_data('task_folder/schema', 'task_folder/event/')


