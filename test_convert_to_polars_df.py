import pytest
import polars as pl
from polars.testing import assert_frame_equal, assert_series_equal
from dictionaries import convert_to_polars_df


def test_normal_input():
    sample_data = [(1, 2), (3, 4)]
    expected_output = pl.DataFrame(
        {"column_0": [1, 2], "column_1": [3, 4]}
    )  # Corrected expected values
    pl.testing.assert_frame_equal(convert_to_polars_df(sample_data), expected_output)


def test_empty_input():
    sample_data = []
    expected_output = pl.DataFrame()
    pl.testing.assert_frame_equal(convert_to_polars_df(sample_data), expected_output)


def test_multiple_entries():
    sample_data = [("a", 1), ("a", 2), ("a", 3)]
    expected_output = pl.DataFrame({"column_0": ["a", "a", "a"], "column_1": [1, 2, 3]})
    pl.testing.assert_frame_equal(convert_to_polars_df(sample_data), expected_output)


def test_invalid_input_data():
    with pytest.raises(TypeError):
        convert_to_polars_df("invalid data")


def test_incorrect_tuple_length():
    sample_data = [("a", 1, "extra"), ("b", 2)]
    with pytest.raises(ValueError):
        convert_to_polars_df(sample_data)
