import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dir_path = os.path.dirname(os.path.realpath(__file__))

data = pd.read_excel(r'C:\Users\admin\Desktop\scraping\23-12-2022.xlsx')
path = r"C:\Users\admin\Desktop\scraping\test.xlsx"

# data1 = data[["Item_code","Model Name","Poorvika price"]]

# print(data1)

# Product header name
print("Header :",data.keys()[4])

# Product total count
# print("Product Count :",len(data))

# product id check

# product_id = data["Item_code"]

# print(product_id)

# print(product_id.isnull().value_counts())

#price compection

# c_price = data[["Poorvika price","Flipkart Price"]]

# print("Poorvika price :",c_price["Poorvika price"].isna().value_counts())
# print("Flipkart Price :", c_price["Flipkart Price"].isna().value_counts())
# print("Flipkart Price :", c_price["Flipkart Price"].fillna(0))

# c_price["flipkart price zero add "] = c_price["Flipkart Price"].fillna(0)
# print(c_price)


# c_price["flipkart equal price"] = c_price["Poorvika price"] == c_price["Flipkart Price"]

# c_price["flipkart greater price"] = c_price["Poorvika price"] > c_price["Flipkart Price"]

# c_price["flipkart lesser price"] = c_price["Poorvika price"] < c_price["Flipkart Price"]

# c_price.loc[(c_price["Poorvika price"] == c_price["Flipkart Price"]),"flipkart equal value"] = c_price["Poorvika price"] - c_price["Flipkart Price"]

# c_price.loc[(c_price["Poorvika price"] > c_price["Flipkart Price"]),"flipkart greater value"] = c_price["Poorvika price"] - c_price["Flipkart Price"]

# c_price.loc[(c_price["Poorvika price"] < c_price["Flipkart Price"]),"flipkart lesser value"] = c_price["Flipkart Price"] - c_price["Poorvika price"]




# c_price.to_excel(path)

