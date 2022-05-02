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

def Most_Common_Streaming_Plat():
    with open(MOVIES_FILE_PATH, "r") as data:
        platforms = []
        series = {}
        #reader = csv.DictReader(data, delimiter=",")
        header = data.readline().rstrip().split(",")
        content = data.readlines()
    
        for element in range(len(content)):
            content[element] = content[element].rstrip().split(",")
        
            dataS = {}
        
            for column in range(len(header)):
                dataS[header[column]] = content[element][column]

            series.update(dataS)

            platforms.append(str([series['PLATFORM']]).replace("[","").replace("]","").replace("'",""))
    
        platform_concurrency = {}
    
        for streaming_plat in platforms:
            if streaming_plat in platform_concurrency:
                platform_concurrency[streaming_plat] += 1
            else:
                platform_concurrency[streaming_plat] = 1
        
        pc_counter = {key: value for (key, value) in sorted(platform_concurrency.items(), key=lambda x: x[1], reverse=True)}
        pc_counter = list(pc_counter)

        return print("The platform in which you have concurred most of the time is:", pc_counter[0])

def Finished_Series_Counter():
    with open(MOVIES_FILE_PATH, "r") as data:
        Finished_series = 0
        series = {}
        #reader = csv.DictReader(data, delimiter=",")
        header = data.readline().rstrip().split(",")
        content = data.readlines()
    
        for element in range(len(content)):
            content[element] = content[element].rstrip().split(",")
        
            dataS = {}
        
            for column in range(len(header)):
                dataS[header[column]] = content[element][column]

                if dataS[header[column]].lower() == 'finished':
                    Finished_series += 1
                else:
                    Finished_series = Finished_series
        
        return print("You have finished a total of: " + str(Finished_series) + " series.")
