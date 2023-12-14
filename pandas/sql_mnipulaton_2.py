import pandas as pd
from sqlalchemy import create_engine

# Connect to your SQL database
# Replace 'your_username', 'your_password', 'your_host', 'your_database' with your actual database credentials
engine = create_engine('postgresql://your_username:your_password@your_host/your_database')

# Load data from a SQL table into a Pandas DataFrame
query = 'SELECT * FROM your_table;'
data = pd.read_sql(query, engine)

# Display the first few rows of the dataframe
print("Original Data:")
print(data.head())

# Perform SQL-like manipulations using Pandas
# For example, filter data based on a condition
filtered_data = data[data['Column1'] > 50]

# Group data and calculate aggregate functions
grouped_data = data.groupby('Category').agg({'Column2': 'mean', 'Column3': 'sum'})

# Display the manipulated data
print("\nManipulated Data:")
print(filtered_data.head())
print("\nGrouped Data:")
print(grouped_data)

# Save the manipulated data to a new SQL table
filtered_data.to_sql('filtered_table', engine, index=False, if_exists='replace')

# Close the database connection
engine.dispose()
