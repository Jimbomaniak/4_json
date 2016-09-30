import json


def load_data():
    filepath = input('Write your path to directory with json file(like c:/users/bars.json): ')
    try:
        with open(filepath) as file:
            data = json.load(file)
        return data 
    except FileNotFoundError:
        print('No such file in directory')
        return load_data()

def pretty_print_json(data):
    print(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',',':')))


if __name__ == '__main__':
    data = load_data()
    pretty_print_json(data)
    
