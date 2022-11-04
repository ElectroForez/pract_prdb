import os
import pandas as pd
from config import src_path, output_path


table_input = os.path.join(src_path, 'Заказы_import.xlsx')
table_output = os.path.join(output_path, 'Заказы_услуги_import.csv')

df = pd.read_excel(table_input)

df['Код заказа'] = df['Код заказа'].apply(lambda x: x.split('/')[0])

order_services = []
for index, row in df.iterrows():
    order_id = row['Код заказа']
    services = row['Услуги'].split(',')
    for service_id in services:
        service_id = service_id.strip()
        order_services.append([order_id, service_id])

new_df = pd.DataFrame(order_services, columns=['Код заказа', 'Код услуги'])


new_df.to_csv(table_output, index=False)
print(new_df)
print(new_df.info())
