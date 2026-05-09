# !pip install pandas

import pandas as pd


vehicle_data = {
    "brand": ["Toyota","Honda","Ford","Chevrolet","BMW"],
    "model": ["Corolla","Civic","F-150","Camaro","X5"],
    "year": [2020,2021,2022,2023,2024],
    "price": [20000,25000,30000,35000,40000]
}

df = pd.DataFrame(vehicle_data)
print(df[df["brand"] == "Toyota"])
df2 = pd.read_csv("vehicle_data.csv")


what all means data cleaning?

