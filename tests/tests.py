## test code

import os.path as path
from dftoltx import generator
import pandas as pd

two_up =  path.abspath(path.join("", 'tests/data.csv'))

df = pd.read_csv(two_up)
df.name = "Excercise Data"

print(df.to_string())

print("--------------")

print(generator.convert_to_tex(df))