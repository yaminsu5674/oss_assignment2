import os
import json
import yaml


print('Please enter the filename you want to convert with extension :', end=' ')
name = input()
filename, file_extension = os.path.splitext(name)
if file_extension == '.yaml':
    with open('in.yaml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    with open('out.json', 'w') as f:
        json.dump(data, f, indent=2)
    print('Successfully converted!')

elif file_extension == '.yml':
    with open('in.yml') as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    with open('out.json', 'w') as f:
        json.dump(data, f, indent=2)
    print('Successfully converted!')

elif file_extension == '.json':
    with open("in.json", "r") as f:
        data = json.load(f)
    with open('out.yaml', 'w') as f:
        yaml.dump(data, f)
    print('Successfully converted!')

else:
    with open("in.jsn", "r") as f:
        data = json.load(f)
    with open('out.yaml', 'w') as f:
        yaml.dump(data, f)
    print('Successfully converted!')
