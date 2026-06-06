import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.describe())
missing = train.isnull().sum()
# print(missing)
print(missing[missing > 0])

#Data cleaning
# train["LotFrontage"] = train["LotFrontage"].fillna((train["LotFrontage"].mean))
# missing = train["LotFrontage"].isnull().sum()
# print(missing)


