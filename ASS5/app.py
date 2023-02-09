import numpy as np
import pandas as pd

file = pd.read_csv("./ASS5/spam.csv",encoding="ISO-8859-1")

file.drop(columns=["Unnamed: 2","Unnamed: 3","Unnamed: 4"], inplace=True)


file.rename(columns={"v1":"status","v2":"message"}, inplace=True)

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

file.drop_duplicates(keep="first")