import pytest
from main import generate_sample_data


def test_sample_data_length():
    size = 10
    max_list_length = 5
    data = generate_sample_data(size, max_list_length)
    assert len(data) <= size * max_list_length
    assert len(data) >= size


def test_sample_data_key_length():
    data = generate_sample_data(10, 5)
    for key, _ in data:
        assert len(key) == 3


def test_sample_data_value_type():
    data = generate_sample_data(10, 5)
    for _, value in data:
        assert type(value) == int


def test_zero_size():
    with pytest.raises(ValueError):
        generate_sample_data(0, 5)


def test_zero_max_list_length():
    with pytest.raises(ValueError):
        generate_sample_data(5, 0)


def test_large_values():
    data = generate_sample_data(1000, 1000)
    assert len(data) <= 1000 * 1000


def test_negative_values():
    with pytest.raises(ValueError):
        generate_sample_data(-1, -1)


def test_non_integer_values():
    with pytest.raises(TypeError):
        generate_sample_data("size", "max_list_length")
