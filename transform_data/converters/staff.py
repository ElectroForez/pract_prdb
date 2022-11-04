import os
import pandas as pd
from config import src_path, output_path


table_input = os.path.join(src_path, 'Сотрудники_import.xlsx')
table_output = os.path.join(output_path, 'Сотрудники_import.csv')

df = pd.read_excel(table_input)

df['Код сотрудника'] = df['Код сотрудника'].apply(lambda x: x.split()[1])
df['Последний вход'] = pd.to_datetime(df['Последний вход'])


df.to_csv(table_output, index=False)
print(df)
print(df.info())