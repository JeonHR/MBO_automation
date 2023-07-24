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



print("unused txt file이 삭제 완료 되었습니다. ")
time.sleep (2)

########################################


def merge_txt_files(Merged_input_path, Merged_output_file):
    with open(Merged_output_file, 'w', encoding='utf-8') as Mereged_outfile:
        for i in range(1, 17):  # site 1 ~16
            merge_file_name = f"{Merged_input_path}/site{i}.txt"  # site{i}.txt 
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

def txt_to_excel(Mer_txt_file, pathloss_excel_file, sheet_name):
    # txt file read & save
    with open(Mer_txt_file, 'r') as Mer_file:
        txt_content_ex = Mer_file.read()

    # data Frame conversion
    df = pd.DataFrame([txt_content_ex], columns=['Content'])

    # excel file load
    writer = pd.ExcelWriter(Pathloss_excel_file_path, mode='a', engine='openpyxl')

    # add excel sheet
    df.to_excel(writer, sheet_name=sheet_name, index=False)

    # save & close
    writer.save()
    writer.close()

Mer_txt_file_path = './Merge.txt'
Pathloss_excel_file_path = './ko.xlsx'
pathloss_selected_sheet_name = 'Sheet1'  

txt_to_excel(Mer_txt_file_path, Pathloss_excel_file_path, pathloss_selected_sheet_name)
print("Merge txt가 excel file에 복사가 완료 되었습니다.")
time.sleep(2)


##############################################

print(current_directory)

folder_path = "./excel"
excel_file = os.path.join(current_directory, folder_path, 'ko.xlsx')
df = pd.read_excel(excel_file, sheet_name = 'ko')
print (df)