import json

def load_from_json(filename):
    with open(filename, 'r') as json_file:
        DATAfromCFG = json.load(json_file)
    return DATAfromCFG

