import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.describe())
missing = train.isnull().sum().sum
print(missing)


#Data cleaning

