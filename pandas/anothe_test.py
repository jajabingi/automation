import pandas as pd
import pytest
from data_manipulation import manipulate_data


def manipulate_data(data):
    # Your data manipulation logic here
    data['New_Column'] = data['Existing_Column'] * 2
    return data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'Existing_Column': [1, 2, 3, 4, 5]
    })

def test_manipulate_data(sample_data):
    # Call the function you want to test
    manipulated_data = manipulate_data(sample_data)

    # Assert that the output meets your expectations
    expected_result = pd.DataFrame({
        'Existing_Column': [1, 2, 3, 4, 5],
        'New_Column': [2, 4, 6, 8, 10]
    })

    pd.testing.assert_frame_equal(manipulated_data, expected_result)

@pytest.mark.parametrize('input_data, expected_result', [
    (pd.DataFrame({'Existing_Column': [1, 2, 3]}), pd.DataFrame({'Existing_Column': [1, 2, 3], 'New_Column': [2, 4, 6]})),
    (pd.DataFrame({'Existing_Column': [5, 10, 15]}), pd.DataFrame({'Existing_Column': [5, 10, 15], 'New_Column': [10, 20, 30]})),
])
def test_manipulate_data_parameterized(input_data, expected_result):
    manipulated_data = manipulate_data(input_data)
    pd.testing.assert_frame_equal(manipulated_data, expected_result)

# Example of mocking external dependencies
@pytest.mark.parametrize('external_dependency_result', [42, 99])
def test_manipulate_data_with_mock(sample_data, external_dependency_result, mocker):
    # Mock an external dependency (e.g., a function that returns a value)
    mocker.patch('data_manipulation.external_dependency_function', return_value=external_dependency_result)

    # Call the function you want to test
    manipulated_data = manipulate_data(sample_data)

    # Assert that the function uses the mocked result as expected
    expected_result = pd.DataFrame({
        'Existing_Column': [1, 2, 3, 4, 5],
        'New_Column': [2, 4, 6, 8, 10],
        'External_Column': [external_dependency_result] * 5
    })

    pd.testing.assert_frame_equal(manipulated_data, expected_result)
