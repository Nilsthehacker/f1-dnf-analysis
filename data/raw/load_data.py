import os
import pandas as pd



#Finds absolute directory path of current file
raw_dir = os.path.dirname(os.path.abspath(__file__))

#Finds path to dataset
csv_path = os.path.join(raw_dir, "f1_dnf.csv")

#Reads csv file into a pandas dataframe
df = pd.read_csv(csv_path)


print(df.head())
print(df.shape) 