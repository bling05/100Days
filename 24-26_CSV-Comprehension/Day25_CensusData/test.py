# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# print(data)


# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp': temperatures.append(row[1])


import pandas

data = pandas.read_csv("weather_data.csv")
temp_list = data.temp.to_list()

# print(data[data.temp == max(data.temp)])

monday = data[data.day == 'monday']
print(int(monday.temp) * 9/5 + 32)