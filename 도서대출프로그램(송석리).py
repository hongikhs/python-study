import csv
import datetime
data = open('학급문고.csv')
file = csv.reader(data)
header = next(file)
file = list(file)
data.close()
for row in file :
    if row[-2] != '' :
        if datetime.datetime.strptime(row[-2], '%Y-%m-%d') < datetime.datetime.now() :
            row[-1] = '연체중'
        
while True :
    menu = input('원하시는 메뉴를 선택해주세요.\n[메뉴]\n1. 대출\n2. 반납\n3. 도서현황\n0. 종료')
    # 도서현황
    if menu == '3' :
        print(header)
        for row in file :
            print(row)
        continue
    if menu == '0' :
        break
        
    no = input('학생 번호를 입력해주세요 :')
    if menu == '1' :
        name = input('대출하실 도서 이름을 입력해주세요 :')
        for row in file :
            if name in row[2] :
                if row[-3] != '' :
                    print('이미 대출 중인 도서입니다.')
                else :
                    row[-4] = '대출중'
                    row[-3] = no
                    r = datetime.datetime.now() + datetime.timedelta(days=14)
                    row[-2] = str(r.year)+'-'+str(r.month)+'-'+str(r.day)
                    print('대출되었습니다. ')
                break
                
    elif menu == '2' :
        print(header)
        for row in file :
            if row[-3] == no :
                print(row)
        name = input('반납하실 도서 이름을 입력해주세요 :')
        for row in file :
            if name in row[2] :
                if row[-3] == no :
                    row[-4] = ''
                    row[-3] = ''
                    row[-2] = ''
                    row[-1] = ''
                    print('반납되었습니다.')
                else :
                    print('대출하신 도서가 아닙니다.')
                break
data = open('학급문고.csv','w',newline = '')
save = csv.writer(data)
save.writerow(header)
for row in file :
    save.writerow(row)
print('저장되었습니다.')
data.close()
