# -*- coding: utf-8 -*-

"""
@author: Mr_zhang
@software: PyCharm
@file: demo_m.py
@time: 2021/8/24 下午2:18
"""

import os
import json
import pandas as pd


base_dir = os.path.dirname(__file__)
file_name = os.path.join(base_dir, 'ICP-domain8-23.xlsx.json')


with open(file_name, 'r') as f:
    res = json.loads(f.read()).get('data')
    
    

r = pd.DataFrame(res)
#
print(r)
r.to_excel('ab.xls', index=False)
