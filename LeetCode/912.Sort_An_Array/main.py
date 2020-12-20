#!/usr/bin/python
from solution import *

# Unit Test
v1 = [1,2,2,3]
v2 = [6,5,4,4]

ms = Merge()
if (ms.sortArray(v1)!=sort(v1)):
    print("Test Failed")
if (ms.sortArray(v2)!=sort(v2)):
    print("Test Failed")