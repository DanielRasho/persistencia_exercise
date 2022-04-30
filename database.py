from tempfile import NamedTemporaryFile
import shutil
import csv

FIELDS = [
"NAME",
"STATE", 
"EPISODE DURATION", 
"WATCHED_EPISODES", 
"PLATFORM", 
"TIME INVESTED"
]

MOVIES_FILE_PATH = "data/movies.csv"

def add_series():
    pass

def delete_series():
    pass

def update_series():
    pass

def get_series():
    pass

def update_series_fields():
    tempfile = NamedTemporaryFile("w+t", newline='', delete=False)

    with open(MOVIES_FILE_PATH, "r") as data, tempfile:
        reader = csv.reader(data, delimiter=",")
        writer = csv.writer(tempfile, delimiter=",")
        
        for line, row in enumerate(reader):
            if line == 0:
                writer.writerow(FIELDS)
            else:
                writer.writerow(row)
    shutil.move(tempfile.name, MOVIES_FILE_PATH)

if __name__ == "__main__":
    update_series_fields()
