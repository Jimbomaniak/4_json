import json


def load_data(filepath):
    try:
        with open(filepath) as file:
            data = json.load(file)
        return data 
    except FileNotFoundError:
        return 'No such file in directory'


def pretty_print_json(data):
    pretty_json = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':'))
    return pretty_json


if __name__ == '__main__':
    filepath = input('Write your path to directory with json file(like c:/users/bars.json): ')
    data = load_data(filepath)
    print(pretty_print_json(data))
    
