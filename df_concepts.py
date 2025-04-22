"""Create empty df"""
import pandas as pd
empty_df = pd.DataFrame()
# print(f"empty_df:::::{empty_df}")


"""df with columns"""
cols = ['col1', 'col2', 'col3']
df_cols = pd.DataFrame(columns=cols)
# print(f"df_cols:::::{df_cols}")

"""df with cols specified"""
data_types = {"col1":'int','col2':'str','col3':'float'}
df_cols_spec = pd.DataFrame({col:pd.Series(dtype=dt) for col,dt in data_types.items()})
# print(f"df_cols_spec:::::::::::::{df_cols_spec}")

"""dict to df"""
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data=data)
# print(f"df:{df}")


"""You have sales data for multiple products over several months in a long format, with columns Month, Product_ID, and Sales.
 You want to transform this data into a wide format where each product has its own column, and each row represents a month.
How would you pivot this DataFrame to achieve the desired format?"""

data = {
    'Month': ['Jan', 'Jan', 'Feb', 'Feb', 'Mar', 'Mar'],
    'Product_ID': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Sales': [100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data)
df_pivot = df.pivot(index='Month', columns='Product_ID', values='Sales')

print(df_pivot)