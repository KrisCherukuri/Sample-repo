import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

ipl_data = pd.read_csv("D:/Python/Desktop/ipl/deliveries.csv")
pd.set_option('display.max_columns',500)
print(ipl_data.head(10))
print(ipl_data.info())

