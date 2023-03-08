# Introduction
What is Pytest?
Pytest is the most popular package for testing code in Python.

## Others
We can run our test using the command: ```pytest /path/of/file/tests/file.py -v```
with the flag v we ensure that the output of test will be more explicative and informative.
 ### Flags 
- ```-p``` If we use the flag: **-p** with the arguments **no:warnings** , so we have the flag with arguments: ```-p no:warnings``` and 
  pytest will ignore the warnings and will not issue warnings.
- ```-m``` custom_name_mark the **m** flag only run the test with the mark with the name custom_name_mark and the others will be ignored. 
  If we run a test with the prefix **not** in the name of custom mark our test with the custom mark will be ignored and the others test without this mark
  will be ignored. Example: ```pytest . -v -m "not my_custom_mark_name"```
- ```-s```: If we run the test with this flag, the flag ```-s``` we can see the prints in the tests


# About Unit testing and Integration Testing


Unit test is about to validate that the businesss logic of a unit of code is doing what it's supposed to.
So in that sense we are only interested in that isolate code. So we isolate this unit from other component
and then we verify that this unit is doing what it's supposed to do for a fix input.

Integration test is simply a test that is testing multiple units.

 