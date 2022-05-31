import json
from main import interval

def save_harmonogram(harmonogram, file_path):
    with open(file_path, "w") as f:
        data = []
        for item in harmonogram:
            data.append(item.__dict__)
        json.dump(data, f, indent=4, default=str)

def load_harmonogram(file_path):
    harmonogram = []

    with open(file_path) as f:
        try: list = json.load(f)
        except: return False
    
    for dict in list:
        harmonogram.append(interval())

    return harmonogram