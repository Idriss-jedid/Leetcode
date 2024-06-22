# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 19:04:33 2024

@author: 21652
"""

import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
   return pd.DataFrame(student_data, columns=['student_id', 'age'])
    