import os
import pandas as pd
from config import src_path, output_path


table_input = os.path.join(src_path, 'Заказы_import.xlsx')
table_output = os.path.join(output_path, 'Заказы_import.csv')

df = pd.read_excel(table_input)


def to_hours(s: str):
    value, unit = s.split()
    value = int(value)

    if 'мин' in unit:
        value //=60

    return value


df['Код заказа'] = df['Код заказа'].apply(lambda x: x.split('/')[0])
df['Время проката'] = df['Время проката'].apply(to_hours)
df.drop(['ID', 'Услуги'], axis= 1, inplace=True)
# df['Дата создания'] = pd.to_datetime(df['Дата создания'])


df.to_csv(table_output, index=False)
print(df)
print(df.info())