# 2018.1.25 @sohi
# 대학의 휴학생비율과 교수1인당 학생수를 검색하는 프로그램이다.
# 대학을 선택할 때 참고자료가 될 수 있다.
# 고등학생이 관심 있게 프로그래밍 할 수 있는 자료를 찾게 되었다.
# 2015_고등교육기관_일람표
# https://www.data.go.kr/dataset/3038867/fileData.do
# 엑셀 파일을 수정 - 제목을 한행으로, 수치데이터 셀을 숫자로 변경한 csv파일 사용
import csv
import datetime
# 파일 내용 읽어오기
file_name='2015univ.csv'
file = open(file_name,'r',encoding='utf8')
csv_file = csv.reader(file)
header = next(csv_file) # 한줄 한줄 읽는다
data = list(csv_file)   # 다음줄을 목록화 한다
file.close()
# 학교 입력
school = input('학교명을 입력하세요 : (ex 조선대학교 한양대학교)').split()
s1 = 0 #재적학생수 int(row[10])
s2 = 0 #재학생수 int(row[11])
s3 = 0 #휴학생수 int(row[12])
p = 0 #교수수 int(row[13])
for s in school :
    for row in data :
        if s==row[3] and row[5]=='기존' and int(row[13])!=0 and int(row[10])!=0 :
            #본교, 분교1, 제2캠퍼스 등은 하나로 합쳐야 함
            s1 = s1 + int(row[10])
            s2 = s2 + int(row[11])
            s3 = s3 + int(row[12])
            p = p + int(row[13])
    
    print(s + ': 휴학생 비율='+str(int(s3/s1*100))+'%' #휴학생비율 = 휴학생수/재적학생수
          + ', 교수1인당 학생수='+str(int(s1/p))+'명('  #교수1인당 학생수 = 재적학생수/교수수
          +str(int(s2/p))+'명)')  #교수1인당 학생수 = 재학생수/교수수
    s1 = s2 = s3 = p = 0
    
