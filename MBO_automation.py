import os
import pandas as pd
import time 
import re


current_directory = os.getcwd()
unused_folder_path = "./unused_txt"

## folder in all file list up
all_unused_txt = os.listdir(unused_folder_path)

## Delete folder in txt.file 
for txt_name in all_unused_txt:
    if txt_name.endswith(".txt"):
        unused_file_path = os.path.join(unused_folder_path, txt_name)
        os.remove(unused_file_path) 


time.sleep (2)
print("unused txt file이 삭제 완료 되었습니다. ")

########################################

# 특정 폴더 경로와 병합 결과를 저장할 파일명 설정
Merged_folder_path = "./"  # 특정 경로
output_file = "merged.txt"  # 병합한 결과를 저장할 파일



def merge_txt_files(Merged_folder_path, output_file):
    # fold in all file
    Merged_file = os.listdir(Merged_folder_path)

    # 파일을 읽어서 데이터를 리스트로 저장
    merged_data = []
    for Merge_file_name in Merged_file:
        if Merge_file_name.endswith(".txt"):
            file_path = os.path.join(Merged_folder_path, Merge_file_name)
            with open(Merged_folder_path, 'r') as Merge_file:
                lines = Merge_file.readlines()
                # 개행 문자 제거 후 데이터를 병합할 리스트에 추가
                merged_data.extend(lines)

    # 병합한 데이터를 새로운 파일에 쓰기
    with open(output_file, 'w') as new_file:
        for line in merged_data:
            new_file.write(line)

    print(f"모든 .txt 파일을 {output_file}에 병합하여 저장하였습니다.")

# Merge file & path 
Merged_folder_path = "./"  # merge file path
output_file = "merged.txt"  # Result txt file

# Merge txt file 
merge_txt_files(Merged_folder_path, output_file)

##############################################



print(current_directory)

folder_path = "./excel"
excel_file = os.path.join(current_directory, folder_path, 'ko.xlsx')
df = pd.read_excel(excel_file, sheet_name = 'ko')
print (df)