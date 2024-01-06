import pytest
import numpy as np
from dictionaries import convert_to_numpy_array


def test_normal_input():
    sample_data = [(1, 2), (3, 4)]
    expected_output = np.array([[1, 2], [3, 4]])
    np.testing.assert_array_equal(
        convert_to_numpy_array(sample_data), expected_output)


def test_empty_input():
    sample_data = []
    expected_output = np.array([])
    np.testing.assert_array_equal(
        convert_to_numpy_array(sample_data), expected_output)


def test_multiple_entries():
    sample_data = [('a', 1), ('a', 2), ('a', 3)]
    expected_output = np.array([('a', 1), ('a', 2), ('a', 3)])
    np.testing.assert_array_equal(
        convert_to_numpy_array(sample_data), expected_output)


def test_invalid_input_data():
    with pytest.raises(TypeError):
        convert_to_numpy_array("invalid data")


def test_incorrect_tuple_length():
    sample_data = [('a', 1, 'extra'), ('b', 2)]
    with pytest.raises(ValueError):
        convert_to_numpy_array(sample_data)
