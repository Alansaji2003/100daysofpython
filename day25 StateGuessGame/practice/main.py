# # with open("weather_data.csv") as file:
# #     data = file.readlines();
# #     print(data)
#
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperature = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperature.append(int(row[1]))
# #     print(temperature)
#
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # temperature = data["temp"]
# # print(temperature)
# #
# # #the to_dict() method converts a dataFrame to dictionary
# # #Series can be converted into list with to_list() method
# #
# # temp_list = temperature.to_list()
# # print(temp_list)
# # avg = sum(temp_list) / len(temp_list)
# #
# # print(avg)
# # #we can also do data.conditions other than data["conditions"]
# #
# # #we can find avg easily
# # print(data["temp"].mean()) #using like key of dictionary
# # print(data["temp"].max())
# # #we can also do data.conditions other than data["conditions"]
# #
# # print(data.temp) #using like attribute of object
#
# #to print row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# ftemp = monday.temp * 9/5 + 32
# print(ftemp)
#
# #create a data frame from scratch
# students = {
#     "students": ["Amy", "Michel", "Chako"],
#     "Marks": [55,77,88]
# }
#
# data2 = pandas.DataFrame(students)
# print(data2)
#
# #to convert to csv
# data2.to_csv("new_file.csv")
import pandas

#Data analysis on 2018 central park squirrel Data
squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gcount = len(squirrels[squirrels["Primary Fur Color"] == "Gray"])
ccount = len(squirrels[squirrels["Primary Fur Color"] == "Cinnamon"])
bcount = len(squirrels[squirrels["Primary Fur Color"] == "Black"])
new_data = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gcount, ccount, bcount]
}
new_csv = pandas.DataFrame(new_data).to_csv("Squirrel_Sample.csv")