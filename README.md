[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Bugs](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=bugs)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=WaughB_Python-collections&metric=coverage)](https://sonarcloud.io/summary/new_code?id=WaughB_Python-collections) [![codecov](https://codecov.io/gh/WaughB/Python-collections/graph/badge.svg?token=6EV2CYYYZD)](https://codecov.io/gh/WaughB/Python-collections) 


# Python-collections
A look into how the different storage types in Python can effect the performance of the application. 

## Coding standards
Certain standards were maintained to get this project going. 
* Test driven development. 
* Sphinx style DocStrings
* Use of a common logger
* Pushing as much logic into functions as possible, keeping main decluttered
* Error handling baked in from the beginning

## How to run
`main.py` kicks off all of the processes. It will return just a few lines of logs about the average execution time for Python dictionaries, Numpy arrays, and Pandas DataFrame. 


## Pytest
Tests are made for: 
* generate_sample_data
* convert_to_dictionaries
* convert_to_numpy_array
* convert_to_pandas_df
* convert_to_polars_df

Still to do: 
* logger
* speed_tests
* main

## Results

### Creation
At small amounts of data (10x10):

```
2024-01-07 12:31:54,685 - speed_tests - INFO - Function <function convert_to_dictionary at 0x000002A64FDCF1A0> Average execution time (microseconds):   100
2024-01-07 12:31:54,688 - speed_tests - INFO - Function <function convert_to_numpy_array at 0x000002A65026DEE0> Average execution time (microseconds):  200
2024-01-07 12:31:54,720 - speed_tests - INFO - Function <function convert_to_pandas_df at 0x000002A65034F420> Average execution time (microseconds):    1401
2024-01-07 12:31:54,737 - speed_tests - INFO - Function <function convert_to_polars_df at 0x000002A65034F4C0> Average execution time (microseconds):    1000
```

_Ranking for 10x10_
1. Dictionary
2. Numpy
3. Polars
4. Pandas

For 100x100 datasets: 

```
2024-01-07 12:32:23,448 - speed_tests - INFO - Function <function convert_to_dictionary at 0x000001C0050DF1A0> Average execution time (microseconds):   400
2024-01-07 12:32:23,466 - speed_tests - INFO - Function <function convert_to_numpy_array at 0x000001C00555DEE0> Average execution time (microseconds):  1800
2024-01-07 12:32:23,508 - speed_tests - INFO - Function <function convert_to_pandas_df at 0x000001C00563F420> Average execution time (microseconds):    2600
2024-01-07 12:32:23,543 - speed_tests - INFO - Function <function convert_to_polars_df at 0x000001C00563F4C0> Average execution time (microseconds):    2751
```

_Ranking for 100x100_
1. Dictionary
2. Numpy
3. Pandas
4. Polars

For 10000x10000 datasets: 

```
2024-01-07 12:36:16,594 - speed_tests - INFO - Function <function convert_to_dictionary at 0x000001D5F0A1F1A0> Average execution time (microseconds):   165484
2024-01-07 12:39:17,557 - speed_tests - INFO - Function <function convert_to_numpy_array at 0x000001D5F0EBDEE0> Average execution time (microseconds):  83271
2024-01-07 12:40:41,103 - speed_tests - INFO - Function <function convert_to_pandas_df at 0x000001D5F0F9F420> Average execution time (microseconds):    339842
2024-01-07 12:49:13,951 - speed_tests - INFO - Function <function convert_to_polars_df at 0x000001D5F0F9F4C0> Average execution time (microseconds):    275781
```

_Ranking for 10000x10000_
1. Numpy
2. Dictionary
3. Polars
4. Pandas

## TODO
Testing
* testing logger
* testing speed_tests
* testing main

Features
* Add addition
* Add sort
* Add search
* Add graphs of performance difference

Random
* Add dockerfile
* Which ones are accepted by ML frameworks?