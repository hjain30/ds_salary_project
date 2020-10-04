# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 21:59:26 2020

@author: Heena
"""

import glassdoor_webscrapper as gs
import pandas as pd
path = "C:/Users/Heena/Documents/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 20)

df