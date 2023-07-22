

import os
import pandas as pd

# 현재 작업 디렉토리 설정
current_directory = os.getcwd()

# 엑셀 파일 읽기
folder_path = 'excel'
excel_file = os.path.join(current_directory, folder_path, 'ko.xlsx')
sheet_name = 'ko'
df = pd.read_excel(excel_file, sheet_name= 'sheet_name')

# 특정 부분 선택
start_row = 1
end_row = 10
start_column = 'A'
end_column = 'C'
selected_data = df.loc[start_row:end_row, start_column:end_column]

# 텍스트 파일로 저장
txt_file = os.path.join(current_directory, folder_path, '저장.txt')
selected_data.to_csv(txt_file, sep='\t', index=False)

print("변환 완료!")