
import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as pg
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading-score"].tolist()

mean = sum(data) / len(data)
std_daviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_deviation_start,  first_std_deviation_end = mean-std_daviation,mean+std_daviation
second_std_deviation_start,  second_std_deviation_end = mean-(2*std_daviation),mean+(2*std_daviation)
third_std_deviation_start,  third_std_deviation_end = mean-(3*std_daviation),mean+(3*std_daviation)

fig = ff.create_distplot([data],["reading scores"],show_hist=False)
fig.add_trace(pg.Scatter(x=[mean,mean],y=[0,0.17], mode="lines",name="MEAN"))
fig.add_trace(pg.Scatter(x=[first_std_deviation_start, first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDERD DEVIATION"))
fig.add_trace(pg.Scatter(x=[first_std_deviation_end, first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION"))
fig.add_trace(pg.Scatter(x=[second_std_deviation_start, second_std_deviation_start],y=[0,0.17],mode="lines",name="STANDERD DEVIATION"))
fig.add_trace(pg.Scatter(x=[second_std_deviation_end, second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in data if result > first_std_deviation_start and result < first_std_deviation_end ]
list_of_data_within_2_std_deviation = [result for result in data if result > second_std_deviation_start and result < second_std_deviation_end ]
list_of_data_within_3_std_deviation = [result for result in data if result > third_std_deviation_start and result < third_std_deviation_end ]

print("Mean of this data is{}".format(mean))
print("Median of this data is{}".format(median))
print("Mode of this data is{}".format(mode))
print("Standerd deviation of this data is{}".format(std_daviation))
print("{}% of data lies within 1 standard deviation ".format(list_of_data_within_1_std_deviation)*100.0/len(data))
print("{}% of data lies within 2 standard deviation ".format(list_of_data_within_2_std_deviation)*100.0/len(data))
print("{}% of data lies within 3 standard deviation ".format(list_of_data_within_3_std_deviation)*100.0/len(data))
