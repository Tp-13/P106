import plotly.express as px
import csv
import numpy as np

def getDataSource(data_path):
    MarksInPercentage = []
    DaysPresent = []
    with open(data_path) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            MarksInPercentage.append(float(row["Marks In Percentage"]))
            DaysPresent.append(float(row["Days Present"]))
        
    return{"x": MarksInPercentage, "y": DaysPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Attendence VS Grades: ", correlation[0,1])

def setUp():
    data_path = "StudentRoll#Data.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)

setUp()