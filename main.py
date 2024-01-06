# main.py

import random
import string
from logger import log_this
import logging
from dictionaries import generate_sample_data, convert_to_dictionary, convert_to_numpy_array, convert_to_pandas_df
from speed_tests import measure_execution_time

CONST_SIZE = 100
CONST_MAX_LIST_LENGTH = 100

if __name__ == "__main__":
    # Initialize the logger. If no log file is specified, logs will just save to .
    # Other logging levels are logging.DEBUG, logging.WARNING, logging.ERROR, logging.CRITICAL.
    logger = log_this(__name__, level=logging.WARNING)
    logger.info("Program started.")

    # Generate sample data.
    sample_data = generate_sample_data(CONST_SIZE, CONST_MAX_LIST_LENGTH)

    # Convert sample data to different data structures.
    dictionary = convert_to_dictionary(sample_data)
    numpy_array = convert_to_numpy_array(sample_data)
    pandas_df = convert_to_pandas_df(sample_data)

    # Speed tests
    measure_execution_time(convert_to_dictionary, 10000, sample_data)
    measure_execution_time(convert_to_numpy_array, 10000, sample_data)
    measure_execution_time(convert_to_pandas_df, 10000, sample_data)

    logger.info("Program ended.")
