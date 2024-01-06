import datetime
import logging
from logger import log_this

logger = log_this(__name__, level=logging.INFO)


def measure_execution_time(func, repetitions=10, *args, **kwargs):
    total_elapsed_time = datetime.timedelta()
    for _ in range(repetitions):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        total_elapsed_time += end_time - start_time
        logger.debug(f"Repitition: {_} Results: {result}")

    average_elapsed_time = total_elapsed_time / repetitions
    average_elapsed_time_ms = int(
        average_elapsed_time.microseconds)  # Convert to milliseconds
    logger.info(
        f"Function {func} Average execution time (microseconds): {average_elapsed_time_ms}")
