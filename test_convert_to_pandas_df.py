import pytest
import pandas as pd
from dictionaries import convert_to_pandas_df  # Replace with your actual module name


def test_normal_input():
    sample_data = [(1, 2), (3, 4)]
    expected_output = pd.DataFrame({"Key": [1, 3], "Value": [2, 4]})
    pd.testing.assert_frame_equal(convert_to_pandas_df(sample_data), expected_output)


def test_empty_input():
    sample_data = []
    expected_output = pd.DataFrame(columns=["Key", "Value"])
    pd.testing.assert_frame_equal(convert_to_pandas_df(sample_data), expected_output)


def test_multiple_entries():
    sample_data = [("a", 1), ("a", 2), ("a", 3)]
    expected_output = pd.DataFrame({"Key": ["a", "a", "a"], "Value": [1, 2, 3]})
    pd.testing.assert_frame_equal(convert_to_pandas_df(sample_data), expected_output)


def test_invalid_input_data():
    with pytest.raises(TypeError):
        convert_to_pandas_df("invalid data")


def test_incorrect_tuple_length():
    sample_data = [("a", 1, "extra"), ("b", 2)]
    with pytest.raises(ValueError):
        convert_to_pandas_df(sample_data)
