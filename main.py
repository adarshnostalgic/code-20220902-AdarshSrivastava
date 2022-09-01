import numpy as np
import pandas as pd
data=[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
df1=pd.DataFrame(data)  # Converting JSON to DataFrame
df1["Heightm"]=df1["HeightCm"]/100        # Converting height to meters
df1.drop(columns="HeightCm", inplace=True) #Drop heights in cm from table
df1["BMI"]=df1["WeightKg"]/(df1["Heightm"]**2)  #Calculating BMI
no_of_over_weight=np.sum((df1['BMI'] >= 25) & (df1['BMI']<=29.9))  # Calculating no. of Over weights

