from tempfile import NamedTemporaryFile
import shutil
import csv

MOVIES_FIELDS = {
"NAME": str,
"STATE": str, 
"EPISODE DURATION": int, 
"WATCHED_EPISODES": int, 
"PLATFORM": str, 
"TIME INVESTED": int
}

MOVIES_FILE_PATH = "data/movies.csv"

def add_series(name, state, episode_duration, watched_episodes, platform):
    time_invested = int(episode_duration) * int(watched_episodes)
    with open(MOVIES_FILE_PATH, "a") as data:
        writer = csv.writer(data, MOVIES_FIELDS.keys())
        writer.writerow([name, state, episode_duration, watched_episodes, platform, time_invested])

def delete_series(series_name:str):
    tempfile = NamedTemporaryFile("w+t", newline='', delete=False)

    with open(MOVIES_FILE_PATH, "r") as data, tempfile:
        reader = csv.DictReader(data, delimiter=",")
        writer = csv.DictWriter(tempfile, MOVIES_FIELDS.keys(), delimiter=",")
        
        writer.writeheader()

        for item in reader:
            if item.get("NAME") != series_name:
                writer.writerow(item)

    shutil.move(tempfile.name, MOVIES_FILE_PATH)

def update_series(series_name:str, field_to_modify:str, new_value:str):
    tempfile = NamedTemporaryFile("w+t", newline='', delete=False)

    with open(MOVIES_FILE_PATH, "r") as data, tempfile:
        reader = csv.DictReader(data, delimiter=",")
        writer = csv.DictWriter(tempfile, MOVIES_FIELDS.keys(), delimiter=",")
        
        writer.writeheader()
    
        for item in reader:
            if item.get("NAME") == series_name:
                item[field_to_modify] = new_value
                writer.writerow(item)
            else:
                writer.writerow(item)
    shutil.move(tempfile.name, MOVIES_FILE_PATH)

def update_series_fields():
    tempfile = NamedTemporaryFile("w+t", newline='', delete=False)

    with open(MOVIES_FILE_PATH, "r") as data, tempfile:
        reader = csv.reader(data, delimiter=",")
        writer = csv.writer(tempfile, delimiter=",")
        
        for line, row in enumerate(reader):
            if line == 0:
                writer.writerow(MOVIES_FIELDS.keys())
            else:
                writer.writerow(row)
    shutil.move(tempfile.name, MOVIES_FILE_PATH)

def get_series(series_name:str):
    with open(MOVIES_FILE_PATH, "r") as data:
        reader = csv.DictReader(data, delimiter=",")
        for item in reader:
            if item.get("NAME") == series_name:
                return item

def get_series_items_names():
    items = []
    with open(MOVIES_FILE_PATH, "r") as data:
        reader = csv.DictReader(data, delimiter=",")
        for item in reader:
            items.append(item.get("NAME"))
    return items

def get_platforms():
    items = []
    with open(MOVIES_FILE_PATH, "r") as data:
        reader = csv.DictReader(data, delimiter=",")
        for item in reader:
            if item.get("PLATFORM") not in items:
                items.append(item.get("PLATFORM"))
    return items

def is_series_saved(series_name:str):
    for series in get_series_items_names() :
        if series_name.upper() == series.upper():
            return True
    return False

if __name__ == "__main__":
    print(is_series_saved("hola"))