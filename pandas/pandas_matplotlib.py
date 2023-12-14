import pandas as pd

# Load data from CSV files
data = pd.read_csv('your_data.csv')

# Convert a column to datetime if applicable
data['Date_Column'] = pd.to_datetime(data['Date_Column'])

# Extract year and month from the datetime column
data['Year'] = data['Date_Column'].dt.year
data['Month'] = data['Date_Column'].dt.month_name()

# Create a new column based on conditional statements
data['Category_Type'] = data['Category_Column'].apply(lambda x: 'High' if x > 50 else 'Low')

# Calculate cumulative sum for a specific column
data['Cumulative_Sum'] = data['Value_Column'].cumsum()

# Apply a function to multiple columns
def complex_transformation(row):
    # Your complex logic here
    return row['Column_A'] * row['Column_B'] + row['Column_C']

data['Transformed_Columns'] = data.apply(complex_transformation, axis=1)

# Display the updated data
print("Updated Data:")
print(data.head())

# Perform additional analysis or visualization as needed
# For example, create a line plot of the cumulative sum over time
import matplotlib.pyplot as plt

plt.plot(data['Date_Column'], data['Cumulative_Sum'])
plt.title('Cumulative Sum Over Time')
plt.xlabel('Date')
plt.ylabel('Cumulative Sum')
plt.show()
