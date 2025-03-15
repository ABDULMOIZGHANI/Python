import pandas as pd

# DATAFRAMES is a 2D data
df = pd.DataFrame(
    {"names": ["ABDUL MOIZ", "MOHAMMAD ALI", "AHMAD"], "marks": [97, 65, 73]}
)

# print(df)

# read the data from customers-100 csv file using pandas 

dataFrom_csv = pd.read_csv("data/customers-100.csv")
# print(dataFrom_csv)

# print(dataFrom_csv.head()) # show the output for only top 5 rows
# print(dataFrom_csv.tail()) # show the output for last 5 rows

describe  = dataFrom_csv.describe()
info  = dataFrom_csv.info()

# Print only a single row
singleRow =  dataFrom_csv.iloc[0]
print(singleRow)