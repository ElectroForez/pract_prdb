import os
import pandas as pd
from config import src_path, output_path


table_input = os.path.join(src_path, 'Услуги_import.xlsx')
table_output = os.path.join(output_path, 'Услуги_import.csv')

df = pd.read_excel(table_input)


df.to_csv(table_output, index=False)
print(df)
print(df.info())