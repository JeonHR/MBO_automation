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
