import os
import pandas as pd




current_directory = os.getcwd()


print(current_directory)

folder_path = "./excel"
excel_file = os.path.join(current_directory, folder_path, 'ko.xlsx')
df = pd.read_excel(excel_file, sheet_name = 'ko')
print (df)




print("변환 완료!")