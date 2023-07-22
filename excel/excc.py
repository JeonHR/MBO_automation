import os
import pandas as pd

current_directory = os.getcwd()

folder_path = "./excel"
excel_file = os.path.join(current_directory, folder_path, 'ko.xlsx')
df = pd.read_excel(excel_file, sheet_name = 'ko', engine= 'openpyxl')
print (df)

hbhbh

start_row = 1
end_row = 10
start_column = 1
end_column = d=
selected_data = df.loc['start_row':'end_row', 'start_column':'end_column']

df(selected_data)


txt_file = os.path.join(current_directory, folder_path, 'save.txt')
selected_data.to_xlsl(txt_file, sep='\t', index=False)


print("변환 완료!")