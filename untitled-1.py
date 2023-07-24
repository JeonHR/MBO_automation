
import os
import pandas as pd
import time 
import re

current_directory = os.getcwd()


import pandas as pd

def txt_to_excel(txt_file_path, excel_file_path, sheet_name):
    # txt 파일 읽기
    with open(txt_file_path, 'r') as file:
        data = file.readlines()

    # 데이터 분할 및 리스트로 변환
    data_list = [line.strip().split(',') for line in data]

    # 데이터프레임 생성
    df = pd.DataFrame(data_list)

    # Excel 파일로 저장
    with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a') as writer:
        df.to_excel(writer, sheet_name=sheet_name, index=False, header=False)
        writer.save()  # Save the data to the Excel file

txt_file_path = './merge.txt'  # 실제 파일 경로와 파일명으로 바꾸세요
excel_file_path = './ko.xlsx'  # 실제 파일 경로와 파일명으로 바꾸세요
sheet_name = 'sheet1'  # 원하는 시트 이름으로 바꾸세요

txt_to_excel(txt_file_path, excel_file_path, sheet_name)
print("Merge txt가 excel file에 복사가 완료 되었습니다.")

time.sleep(2)