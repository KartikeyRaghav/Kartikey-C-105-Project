import math
import csv

def mean(data):
    return sum(data)/len(data)

with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
    new_data = []
    for i in range(len(file_data[0])):
        data = file_data[0][i]
        new_data.append(float(data))

    squared_list = []
    for x in new_data:
        diff = x - mean(new_data)
        sq = diff**2
        squared_list.append(sq)
    variance = sum(squared_list)/(len(squared_list)-1)
    std_deviation = math.sqrt(variance)
    print(std_deviation)