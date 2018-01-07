import os
import csv
import datetime
import sys
# 참고
# datetime.datetime.strptime( ~ , "%Y-%m-%d", )
# datetime.datetime.now()
#---------[세팅영역]-----------
# 데이터 예제 샘플 파일 이름
data_file = "test.txt"
data_file_encoding = 'utf8'
max_book_checkout_count = 3
checkout_days = 7
#---------[함수 정의]-----------
# 샘플 파일 생성 함수
def make_samplefile_one():
    file = open(data_file, 'w', newline='')
    save = csv.writer(file)    
    save.writerow(['번호','분야','도서명','저자','출판사','발행일','대출여부','대출학생이름','반납예정일','연체여부'])
    save.writerow(['1','IT/개발','게임 프로그래밍 패턴','로버트 나이스트롭','한빛미디어','2016.06.01.','','','',''])
    save.writerow(['2','IT/개발','나는 프로그래머다 2','임백준, 정도현, 김호광','한빛미디어','2016.07.01.','','','',''])
    save.writerow(['3','IT/개발','핵심만 골라배우는 안드로이드 3 & 프로그래밍','닐 스미스','제이펍','2017.08.14.','','','',''])
    save.writerow(['4','IT/개발','벤츠타는 프로그래머','정금호','제이펍','2013.08.26.','','','',''])
    save.writerow(['5','IT/개발','실용주의 프로그래머','앤드류 헌트','인사이트','2014.03.28.','','','',''])
    save.writerow(['6','IT/개발학','피플웨어(3판)','톰 드마르코','인사이트','2014.07.15.','','','',''])
    save.writerow(['7','수필','작가의 수지','모리 히로시','북스피어','2017.01.15.','','','',''])
    print('예제파일 ' + data_file + ' 생성 완료')
# 가로 바 출력 함수-------------------------
def print_hr():
    print('-----------------------------------------------------------------------')
    
# 넘겨진 객체 내용을 모두 출력하는 함수
def print_books(datas):
    for data in datas:
        print( data )
    
    
#---------[메인 코드]-----------
    
# 데이터 예제 샘플 파일이 있는지 확인하고 없으면 하나 만들기
if os.path.isfile(data_file) == False:
    print('예제 샘플 파일이 없어서 하나 만들께요~')
    make_samplefile_one()
# CSV로 된 데이터 파일 읽어서 리스트로 저장하기
file = open(data_file, encoding=data_file_encoding)
file_csv = csv.reader(file)
header = next(file_csv)
datas = list(file_csv)
file.close()
# 제대로 불러왔는지 궁금하면 아래 주석 해제, 테스트
# print_books(datas)
# 프로그램 제목 찍기
print_hr()
print("#### 도서대출반납 시스템 ####")
print_hr()
# 사용자 이름 물어본 후 환영 인사
user_name = input("> 이름을 입력하세요 : ")
print(user_name, "님, 반갑습니다. =)")
while(True):
    print_hr()
    # 개인 대출 상황을 출력
    user_checkout_book_cnt = 0
    user_checkout_timeout_book_cnt = 0
    nowDate = datetime.datetime.now().strftime('%Y-%m-%d')
    for book in datas:
        if book[6] == 'O' and book[7] == user_name:
            user_checkout_book_cnt = user_checkout_book_cnt + 1
            if (datetime.datetime.strptime(book[8], '%Y-%m-%d') - datetime.datetime.strptime(nowDate, '%Y-%m-%d')).days < 0 :
                user_checkout_timeout_book_cnt = user_checkout_timeout_book_cnt + 1
    print("현재 ", user_checkout_book_cnt, "권을 대출 중입니다.")
    
    if user_checkout_timeout_book_cnt == 0:
        print("현재 ",max_book_checkout_count - user_checkout_book_cnt, "권을 대출이 가능합니다.")
    else:
        print("대출중인 도서 중에 연체 도서가 있습니다! 빨리 반납해주세요!!\n현재 연체 중이라 도서를 대여할 수 없습니다.")
    print_hr()
    print("1.대출 2.반납 0.종료")
    menu = input("> 원하시는 메뉴를 입력하세요 : ")
    print_hr()
    ## 입력 메뉴별 처리
    if menu == '1' :
        # 대출 가능한 도서 체크
        is_book = False;
        for book in datas:
            if book[6] == '':
                is_book = True;
        if(user_checkout_timeout_book_cnt > 0):
            print("대출중인 도서 중에 연체 도서가 있습니다! 빨리 반납해주세요!!\n현재 연체 중이라 도서를 대여할 수 없습니다.")
        elif(user_checkout_book_cnt >= max_book_checkout_count ):
            print("현재", max_book_checkout_count,"권 대출 중으로 최대 대출 권 수에 도달했습니다.\n반납을 먼저 해주세요.")
        elif(is_book == False):
            print("대출 가능한 서적이 없습니다. 모두 대출중입니다!")
        else:
            print("대출 가능한 서적이 다음과 같습니다.")
            print("번호\t도서명\t저자\t출판사")
            for book in datas:
                if book[6] == '':
                    print(book[0],'\t',book[2],'\t',book[3],'\t',book[4])
            book_no = input('대출하고자 하는 책 번호를 입력하세요(취소는 c) : ')
            if book_no == 'c' or book_no == '':
                print('도서 대출이 취소되었습니다.')
            else:
                # 도서 대출 처리
                is_bookno_correct = False
                for book in datas:
                    if book[0] == book_no:
                        is_bookno_correct = True
                        if book[6] == '':
                            book[6] = 'O'
                            book[7] = user_name
                            book[8] = (datetime.datetime.now() + datetime.timedelta(days=checkout_days)).strftime('%Y-%m-%d')
                            print(book[2], "도서가 대출되었습니다.")
                            print("도서 반납 날짜는 ",book[8],"입니다.")
                        else:
                            print("해당 도서는 이미 대출중입니다.")
                if is_bookno_correct == False:
                    print("대출하고자 하는 도서 번호를 잘못 입력하셨습니다!")
    elif menu == '2':
        is_book = False
        is_book_no = 0
        for book in datas:
            if book[6] == 'O' and book[7] == user_name:
                is_book_no = is_book_no + 1
        if is_book_no == 0:
            print("반납 할 도서가 없습니다")
        else:
            print("반납할 수 있는 서적은 다음과 같습니다.")
            print("번호\t도서명\t저자\t출판사")
            for book in datas:
                if book[6] == 'O' and book[7] == user_name:
                    print(book[0],'\t',book[2],'\t',book[3],'\t',book[4])
            book_no = input('반납하고자 하는 책 번호를 입력하세요(취소는 c) : ')
            if book_no == 'c' or book_no == '':
                print('도서 반납이 취소되었습니다.')
            else:
                is_bookno_correct = False
                for book in datas:
                    if book[0] == book_no:
                        is_bookno_correct = True
                        if book[6] == 'O':
                            if book[7] == user_name:
                                book[6] = ''
                                book[7] = ''
                                book[8] = ''
                                # book[8] = # 날짜수정해서 반납 예정일 입력
                                print(book[2] + " 도서가 반납되었습니다.")
                            else:
                                print(no + "님이 대출한 도서가 아닙니다!")
                                print("대출한 도서는 본인이 직접 반납해야 합니다.")
                        else:
                            print("해당 도서는 대출중인 책이 아닙니다.")
                if is_bookno_correct == False:
                    print("대출하고자 하는 도서 번호를 잘못 입력하셨습니다!")
    #print_books(datas)
    elif menu == '0':
        break;
    file = open(data_file, 'w', newline='')
    save = csv.writer(file)
    save.writerow(header)
    for data in datas:
        save.writerow( [data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8],data[9]])
    file.close()
print("도서대출반납 시스템이 종료되었습니다.\n이용해주셔서 감사합니다.")
