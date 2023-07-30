import os
import pandas as pd
import time 
import subprocess

### TXT file delete

current_directory = os.getcwd()
unused_folder_path = "./unused_txt"

## folder in all file list up
all_unused_txt = os.listdir(unused_folder_path)

## Delete folder in txt.file 
for txt_name in all_unused_txt:
    if txt_name.endswith(".txt"):
        unused_file_path = os.path.join(unused_folder_path, txt_name)
        os.remove(unused_file_path) 



print("unused txt file이 삭제 완료 되었습니다. ")
time.sleep (2)

########################################


def merge_txt_files(Merged_input_path, Merged_output_file):
    with open(Merged_output_file, 'w', encoding='utf-8') as Mereged_outfile:
        for i in range(1, 17):  # site 1 ~16
            merge_file_name = f"{Merged_input_path}/pathloss_r2_site{i}.txt"  # site{i}.txt 
            try:
                with open(merge_file_name, 'r', encoding='utf-8') as infile:
                    Mereged_outfile.write(infile.read())  # site{i}.txt 파일의 내용을 Merge.txt에 추가
            except FileNotFoundError:
                print(f"File {merge_file_name} not found. Stop.")
                break

if __name__ == "__main__":
    Merged_input_path = "./"  # Merged file path
    Merged_output_file = "Merge.txt"  # Merged file name
    merge_txt_files(Merged_input_path, Merged_output_file)

print("Merged txt로 변환 완료 되었습니다. ")
time.sleep (2)


##############################################



import openpyxl
import time

# 텍스트 파일에서 데이터를 읽어옵니다.
text_file_path = './Merge.txt'
data = []
with open(text_file_path, 'r') as file:
    for line in file:
        data.append(line.strip().split(','))

# 덮어쓰기를 원하는 엑셀 파일과 시트를 지정합니다.
excel_file_path = './Pathloss_Tool.xlsx'
sheet_name = 'go'


# 엑셀 파일을 열고 특정 시트를 가져옵니다.
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook[sheet_name]

# 기존 시트의 내용을 모두 삭제합니다.
for row in sheet:
    sheet.delete_rows(1, sheet.max_row)

# 새로운 데이터를 시트에 추가합니다.
for row_data in data:
    sheet.append(row_data)

# 변경사항을 저장하고 파일을 닫습니다.
workbook.save(excel_file_path)
workbook.close()


print("Merge.txt -> excel 로 변환 완료 되었습니다.! ")
time.sleep(2)
