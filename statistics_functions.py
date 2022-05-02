import csv
from multiprocessing.sharedctypes import Value

MOVIES_FILE_PATH = "data/movies.csv"
#FIND THE SERIES WITH MOST SPENT TIME 
def Most_Watched_Series():
        with open(MOVIES_FILE_PATH, "r") as data:
            series_time_invested = {}
            series = {}
            #reader = csv.DictReader(data, delimiter=",")
            header = data.readline().rstrip().split(",")
            content = data.readlines()
    
        for element in range(len(content)):
            content[element] = content[element].rstrip().split(",")
        
            dataS = {}
        
            for column in range(len(header)):
                dataS[header[column]] = dataS[element][column]

            series.update(dataS)

            series_time_invested[series['NAME']] = series['TIME INVESTED']
    
        most_watched_serie = max(series_time_invested, key=series_time_invested.get)
        
        return print("The serie in which you have invested most time is:",most_watched_serie)
