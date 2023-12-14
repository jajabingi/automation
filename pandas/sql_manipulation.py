import pandas as pd
from sqlalchemy import create_engine

# Connect to your SQL database
engine = create_engine('postgresql://your_username:your_password@your_host/your_database')

# Load data from multiple SQL tables into Pandas DataFrames
query_table1 = 'SELECT * FROM table1;'
query_table2 = 'SELECT * FROM table2;'
data_table1 = pd.read_sql(query_table1, engine)
data_table2 = pd.read_sql(query_table2, engine)

# Display the first few rows of the dataframes
print("Data from Table 1:")
print(data_table1.head())
print("\nData from Table 2:")
print(data_table2.head())

# Perform SQL-like join operation
merged_data = pd.merge(data_table1, data_table2, on='common_column', how='inner')

# Update records in the DataFrame based on a condition
data_table1.loc[data_table1['Column1'] > 50, 'Column2'] = 'Updated Value'

# Use a subquery to filter data
subquery_data = pd.read_sql('SELECT * FROM table1 WHERE Column1 > 50;', engine)

# Display the manipulated and subquery data
print("\nMerged Data:")
print(merged_data.head())
print("\nUpdated Data:")
print(data_table1.head())
print("\nSubquery Data:")
print(subquery_data.head())

# Save the merged data to a new SQL table
merged_data.to_sql('merged_table', engine, index=False, if_exists='replace')

# Close the database connection
engine.dispose()
