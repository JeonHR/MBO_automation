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

##############################
import win32com.client as win32
import os
import time

# Excel 객체 생성
excel = win32.Dispatch("Excel.Application")
excel.Visible = False  # Excel 창을 보이도록 설정 (False로 설정하면 숨김)

try:
    # 현재 작업 디렉토리를 기준으로 상대 경로를 절대 경로로 변환
    relative_path = "./Pathloss_Tool.xlsx"
    absolute_path = os.path.abspath(relative_path)
    

    # 열기
    wb = excel.Workbooks.Open(absolute_path)  # 상대 경로 대신 절대 경로를 사용

    # 원하는 작업 수행 (예: 데이터 수정)

    # 기존 파일에 덮어쓰기로 저장
    wb.Save()

    # 무조건 저장 (변경 사항이 없어도 저장)
    wb.Close(SaveChanges=True)

    # Excel 작업 완료 후 충분한 시간 대기 (예: 2초)
    time.sleep(2)

except Exception as e:
    print(f"오류 발생: {e}")
finally:
    # Excel 종료
    excel.Quit()
    
##############################################
folder_path = "./unused_txt"
folder_path_Pathloss_r2="./"
current_directory = os.getcwd()
excel_file = os.path.join(current_directory, 'Pathloss_Tool.xlsx')

dfs = {}
for i in range(1, 17):
    dfs[i] = pd.read_excel(excel_file, sheet_name=f'site{i}')
    print(f"Data from sheet {i}:")
    print(dfs[i])
    print("site sorting 완료")
    txt_file = os.path.join(current_directory, folder_path, f'site{i}.txt')
    dfs[i].to_csv(txt_file, sep=',', index=False)

print("txt로 저장 완료!")
time.sleep(2)

for i in range(1, 17):
    txt_file = os.path.join(current_directory, folder_path, f'site{i}.txt')
    new_txt_file = os.path.join(current_directory, folder_path_Pathloss_r2, f'pathloss_r2_s{i}.txt')

    with open(txt_file, 'r') as file:
        lines = file.readlines()

    with open(new_txt_file, 'w') as new_file:
        for line in lines:
            new_line = line.replace('"', '') 
            new_file.write(new_line)



print("pathlos_txt, 파일로 변환 완료!")
time.sleep(2)

############################################



def run_perl_program(perl_script_path):

    try:
        subprocess.run(["perl", perl_script_path], check=True)
        print("Perl 프로그램이 성공적으로 실행되었습니다.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

perl_script_path = "./pathloss_put_macmini_r0_20200808.pl"

run_perl_program(perl_script_path)

time.sleep(2)