import pytest
from main import convert_to_dictionary


def test_normal_input():
    sample_data = [("a", 1), ("b", 2), ("a", 3)]
    expected_output = {"a": [1, 3], "b": [2]}
    assert convert_to_dictionary(sample_data) == expected_output


def test_empty_input():
    sample_data = []
    expected_output = {}
    assert convert_to_dictionary(sample_data) == expected_output


def test_multiple_entries_same_key():
    sample_data = [("a", 1), ("a", 2), ("a", 3)]
    expected_output = {"a": [1, 2, 3]}
    assert convert_to_dictionary(sample_data) == expected_output


def test_invalid_input_data():
    with pytest.raises(TypeError):
        convert_to_dictionary("invalid data")


def test_incorrect_tuple_length():
    sample_data = [("a", 1, "extra"), ("b", 2)]
    with pytest.raises(ValueError):
        convert_to_dictionary(sample_data)
