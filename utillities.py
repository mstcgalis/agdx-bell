import json

def save_harmonogram(harmonogram, file_path):
    """saves data into a specified json file, creates one if it doesnt eist

    Args:
        file_path (string): the path of the file
        data (dict, list, tuple, string, int, float, bool): the object to be saved
    """
    with open(file_path, "w") as f:
        data = []
        for item in harmonogram:
            # data = data + json.dumps(item.__dict__, sort_keys=True, indent=4, default=str) + ","
            data.append(item.__dict__)
        json.dump(data, f, indent=4, default=str, sort_keys=True)

def open_file(file_path):
    """opens and parses a json file, which it then returns

    Args:
        file_path (string): the path of the file

    Returns:
        object: data form the file
    """
    with open(file_path) as f:
        try: data = json.load(f)
        except: data = {}
    return data