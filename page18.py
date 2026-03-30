import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('student-mat.csv')

data.head()

data.columns

len(data)

data.info()

data.describe()

data.dtypes

data.isnull().any()

data.corr()
data.corr()['G3']

