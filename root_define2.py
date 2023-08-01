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