# Introduction
What is Pytest?
Pytest is the most popular package for testing code in Python.

## Others
We can run our test using the command: ```pytest /path/of/file/tests/file.py -v```
with the flag v we ensure that the output of test will be more explicative and informative.
 ### Flags 
- If we use the flag: -p no:warnings pytest will ignore the warnings and will not issue warnings.
- -m custom_name_mark the **m** flag only run the test with the mark with the name custom_name_mark and the others will be ignored.
- If we run a test with the prefix **not** in the name of custom mar our test with the custom mark will be ignored and the others test without this mark
  will be ignored. Example: ```pytest . -v -m "not my_custom_mark_name```