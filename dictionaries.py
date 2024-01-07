# dictionaries.py

import random
import string
from logger import log_this
import logging
import numpy as np
import pandas as pd
import polars as pl

logger = log_this(__name__, level=logging.WARNING)


def generate_sample_data(size, max_list_length):
    """
    Generates sample data for a Python dictionary.

    :param size: Number of keys in the dictionary.
    :param max_list_length: Maximum length of the list for each key.
    :return: List of tuples (key, value) where key is a string and value is an integer.
    """
    if size <= 0 or max_list_length <= 0:
        logger.error(
            "Size and max list length must be non-negative, and non-zero.")
        raise ValueError(
            "Size and max list length must be non-negative, and non-zero.")

    try:
        logger.info("Generating sample data.")
        sample_data = []

        for _ in range(size):
            key = ''.join(random.choice(string.ascii_lowercase)
                          for _ in range(3))  # Generate a random 3-letter string
            if max_list_length > 0:
                for _ in range(random.randint(1, max_list_length)):
                    # Generate a random integer between 1 and 100
                    value = random.randint(1, 100)
                    sample_data.append((key, value))
            else:
                # If max_list_length is 0, no values are added for this key
                sample_data.append((key, []))

            logger.debug(sample_data)

    except Exception as sample_data_error:
        logger.error("Error generating sample data: " + str(sample_data_error))
        raise sample_data_error

    logger.info("Successfully generated sample data.")
    logger.debug("Sample Data: " + str(sample_data))
    return sample_data


def convert_to_dictionary(sample_data):
    """
    Converts sample data to a Python dictionary.

    :param sample_data: List of tuples (key, value) where key is a string and value is an integer.
    :return: Python dictionary.
    """
    if not isinstance(sample_data, list):
        logger.error("Sample data must be a list.")
        raise TypeError("sample_data must be a list.")

    try:
        logger.info("Converting sample data to a Python dictionary.")
        dictionary = {}

        for item in sample_data:
            if not isinstance(item, tuple):
                logger.error("Each item in sample data must be a tuple.")
                raise TypeError("Each item in sample_data must be a tuple.")
            if len(item) != 2:
                logger.error(
                    "Each tuple in sample data must contain exactly 2 elements.")
                raise ValueError(
                    "Each tuple in sample_data must contain exactly 2 elements.")

            key, value = item
            if key in dictionary:
                dictionary[key].append(value)
            else:
                dictionary[key] = [value]

    except Exception as convert_to_dictionary_error:
        logger.error("Error converting sample data to a Python dictionary: " +
                     str(convert_to_dictionary_error))
        raise convert_to_dictionary_error

    logger.info("Successfully converted sample data to a Python dictionary.")
    logger.debug("Python dictionary: " + str(dictionary))
    return dictionary


def convert_to_numpy_array(sample_data):
    """
    Converts sample data to a NumPy array.

    :param sample_data: List of tuples where each tuple represents a row in the array.
    :return: NumPy array.
    """
    if not isinstance(sample_data, list):
        logger.error("Sample data must be a list.")
        raise TypeError("sample_data must be a list.")

    try:
        logger.info("Converting sample data to a NumPy array.")

        if not sample_data:
            # Return an empty array equivalent to np.array([])
            return np.array([])

        # Verify that all tuples have the same length
        if len(set(len(item) for item in sample_data if isinstance(item, tuple))) != 1:
            logger.error(
                "All tuples in sample data must have the same length.")
            raise ValueError(
                "All tuples in sample_data must have the same length.")

        # Convert to NumPy array
        np_array = np.array(sample_data)

    except Exception as convert_to_numpy_array_error:
        logger.error("Error converting sample data to a NumPy array: " +
                     str(convert_to_numpy_array_error))
        raise convert_to_numpy_array_error

    logger.info("Successfully converted sample data to a NumPy array.")
    logger.debug("Numpy array: " + str(np_array))
    return np_array


def convert_to_pandas_df(sample_data):
    """
    Converts sample data to a Pandas DataFrame.

    :param sample_data: List of tuples where each tuple represents a row in the DataFrame.
    :return: Pandas DataFrame.
    """
    if not isinstance(sample_data, list):
        logger.error("Sample data must be a list.")
        raise TypeError("sample_data must be a list.")

    try:
        logger.info("Converting sample data to a Pandas DataFrame.")

        if not all(isinstance(item, tuple) and len(item) == 2 for item in sample_data):
            logger.error(
                "Each item in sample data must be a 2-element tuple.")
            raise ValueError(
                "Each item in sample_data must be a 2-element tuple")

        # Creating DataFrame from sample_data
        df = pd.DataFrame(sample_data, columns=['Key', 'Value'])

    except Exception as convert_to_pandas_df_error:
        logger.error("Error converting sample data to a Pandas DataFrame: " +
                     str(convert_to_pandas_df_error))
        raise convert_to_pandas_df_error

    logger.info("Successfully converted sample data to a Pandas DataFrame.")
    logger.debug("Pandas DataFrame: " + str(df))
    return df


def convert_to_polars_df(sample_data):
    """
    Converts sample data to a Polars DataFrame.

    :param sample_data: List of tuples where each tuple represents a row in the DataFrame.
    :return: Polars DataFrame.
    """
    if not isinstance(sample_data, list):
        logger.error("Sample data must be a list.")
        raise TypeError("sample_data must be a list.")

    try:
        logger.info("Converting sample data to a Polars DataFrame.")

        if not sample_data:
            # Return an empty DataFrame
            return pl.DataFrame()

        # Verify that all tuples have the same length
        if len(set(len(item) for item in sample_data if isinstance(item, tuple))) != 1:
            logger.error(
                "All tuples in sample data must have the same length.")
            raise ValueError(
                "All tuples in sample_data must have the same length.")

        # Convert to Polars DataFrame
        df = pl.DataFrame(sample_data)

    except Exception as convert_to_polars_df_error:
        logger.error("Error converting sample data to a Polars DataFrame: " +
                     str(convert_to_polars_df_error))
        raise convert_to_polars_df_error

    logger.info("Successfully converted sample data to a Polars DataFrame.")
    logger.debug("Polars DataFrame: " + str(df))
    return df
