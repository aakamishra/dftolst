# dftoltex or Dataframe to LaTex

This is a simple package written by Aakash Mishra to translate pandas dataframes into LaTex code. Credit of this idea goes to my fellow developer Frank D'Agostino.

## How to Use

```python

from dftoltx import generator
import pandas as pd

df = pd.read_csv(__filename__)
df.name = "Excercise Data"

print(generator.convert_to_tex(df))

```