# main.py

import random
import string
from logger import log_this
import logging
from dictionaries import generate_sample_data
from dictionaries import convert_to_dictionary
from dictionaries import convert_to_numpy_array
from dictionaries import convert_to_pandas_df

CONST_SIZE = 5
CONST_MAX_LIST_LENGTH = 5

if __name__ == "__main__":
    # Initialize the logger. If no log file is specified, logs will just save to .
    # Other logging levels are logging.DEBUG, logging.WARNING, logging.ERROR, logging.CRITICAL.
    logger = log_this(__name__, level=logging.DEBUG)

    logger.info("Program started.")

    sample_data = generate_sample_data(CONST_SIZE, CONST_MAX_LIST_LENGTH)
    logger.debug("Sample Data: " + str(sample_data))

    dictionary = convert_to_dictionary(sample_data)
    logger.debug("Python dictionary: " + str(dictionary))

    numpy_array = convert_to_numpy_array(sample_data)
    logger.debug("Numpy array: " + str(numpy_array))

    pandas_df = convert_to_pandas_df(sample_data)
    logger.debug("Pandas DataFrame: " + str(pandas_df))

    logger.info("Program ended.")
