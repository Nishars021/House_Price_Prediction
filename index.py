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

#BsmtExposure
train["BsmtExposure"] = train["BsmtExposure"].fillna(train["BsmtExposure"].mode)
print(train["BsmtExposure"].isnull().sum())

#BsmtFinType1
train["BsmtFinType1"] = train["BsmtFinType1"].fillna(train["BsmtFinType1"].mode)
print(train["BsmtFinType1"].isnull().sum())

#BsmtFinType1
train["BsmtFinType2"] = train["BsmtFinType2"].fillna(train["BsmtFinType2"].mode)
print(train["BsmtFinType2"].isnull().sum())

#Electrical
train["Electrical"] = train["Electrical"].fillna(train["Electrical"].mode)
print(train["Electrical"].isnull().sum())

