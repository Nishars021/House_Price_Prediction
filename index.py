import pandas as pd
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
# print(train.head())
# print(test.head())
# print(train.info())
# print(test.info())
# print(train.describe())
# missing = train.isnull().sum()
# # print(missing)
# print(missing[missing > 0])

#Data cleaning
#LotFrontage
train["LotFrontage"] = train["LotFrontage"].fillna((train["LotFrontage"].mean))
print(train["LotFrontage"].isnull().sum())

#Alley
train["Alley"] = train["Alley"].fillna(train["Alley"].mode)
print(train["Alley"].isnull().sum())

#MasVnrType
train["MasVnrType"] = train["MasVnrType"].fillna(train["MasVnrType"].mode)
print(train["MasVnrType"].isnull().sum())

#BsmtQual 
train["BsmtQual"] = train["BsmtQual"].fillna(train["BsmtQual"].mode)
print(train["BsmtQual"].isnull().sum())

#BsmtCond
train["BsmtCond"] = train["BsmtCond"].fillna(train["BsmtCond"].mode)
print(train["BsmtCond"].isnull().sum())