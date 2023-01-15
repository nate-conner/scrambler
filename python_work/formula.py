import pandas as pd
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

df = pd.read_csv('topdogsdata.csv')
print(df.to_string())
