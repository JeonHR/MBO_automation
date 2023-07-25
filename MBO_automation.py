import os
import pandas as pd
import time 
import re
import subprocess

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


##############################################



############################################



def run_perl_program(perl_script_path):

    try:
        subprocess.run(["perl", perl_script_path], check=True)
        print("Perl 프로그램이 성공적으로 실행되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

perl_script_path = "./your_perl_script.pl"

run_perl_program(perl_script_path)

