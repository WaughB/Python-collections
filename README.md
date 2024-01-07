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

Still to do: 
* convert_to_pandas_df
* logger
* speed_tests
* main

## Results
At small amounts of data (10x10):

```
2024-01-06 00:11:19,594 - speed_tests - INFO - Function <function convert_to_dictionary at 0x00000255F01093A0> Average execution time (microseconds): 10
2024-01-06 00:11:19,642 - speed_tests - INFO - Function <function convert_to_numpy_array at 0x00000255F1B1D5E0> Average execution time (microseconds): 260
2024-01-06 00:11:20,070 - speed_tests - INFO - Function <function convert_to_pandas_df at 0x00000255F1B1D670> Average execution time (microseconds): 2238
```

For larger amounts of data (100x100): 

```
2024-01-06 00:11:52,508 - speed_tests - INFO - Function <function convert_to_dictionary at 0x00000140BED19430> Average execution time (microseconds): 777
2024-01-06 00:12:13,389 - speed_tests - INFO - Function <function convert_to_numpy_array at 0x00000140C072D670> Average execution time (microseconds): 2055
2024-01-06 00:13:05,421 - speed_tests - INFO - Function <function convert_to_pandas_df at 0x00000140C072D700> Average execution time (microseconds): 3166
```

As small amounts of data, the Python Dictionary is incredibly quick at being setup. As the amount of data increases, the order of performance is maintained but the difference becomes smaller. Furhter testing is needed to see if for even larger sums of data if the relationship stays the same. 

## TODO
Testing
* testing convert_to_pandas_df
* testing logger
* testing speed_tests
* testing main
* testing convert_to_polars_df

Features
* Add polars
* Redo other tests to include polars
* Add addition
* Add sort
* Add search
* Add graphs of performance difference

Random
* Add requirements.txt file
* Add dockerfile
* Which ones are accepted by ML frameworks?