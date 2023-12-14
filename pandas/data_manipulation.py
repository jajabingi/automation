import pandas as pd
import pytest
from data_manipulation import manipulate_data

def manipulate_data(data):
    # Your data manipulation logic here
    data['New_Column'] = data['Existing_Column'] * 2
    return data

def test_manipulate_data():
    # Create a sample DataFrame for testing
    data = pd.DataFrame({
        'Existing_Column': [1, 2, 3, 4, 5]
    })

    # Call the function you want to test
    manipulated_data = manipulate_data(data)

    # Assert that the output meets your expectations
    expected_result = pd.DataFrame({
        'Existing_Column': [1, 2, 3, 4, 5],
        'New_Column': [2, 4, 6, 8, 10]
    })

    pd.testing.assert_frame_equal(manipulated_data, expected_result)

