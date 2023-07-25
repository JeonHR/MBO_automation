
import os
import pandas as pd
import time 
import re


current_directory = os.getcwd()

def txt_to_excel(from_txt_file_path, to_txt_from_excel_file_path, sheet):
    # txt 파일 읽기
    with open(from_txt_file_path, 'r') as from_file:
        data = from_file.readlines()

    # data split and list
    data_list = [line.strip().split(',') for line in data]

    # 데이터프레임 생성
    df = pd.DataFrame(data_list)

    # Excel 파일로 저장
    with pd.ExcelWriter(to_txt_from_excel_file_path, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=sheet, index=False, header=False)

    print(f"data가 {sheet} 시트에 성공적으로 저장되었습니다!")


from_txt_file_path = './Merge.txt'  # file path
to_txt_from_excel_file_path = './ko.xlsx'  # excel path
sheet = 'Sheet1'  # sheet name

txt_to_excel(from_txt_file_path, to_txt_from_excel_file_path, sheet)
print("Merge.txt 파일의 데이터가 Excel 파일에 복사되었습니다.")

time.sleep(2)