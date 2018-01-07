import csv
import datetime
data=open('book_1.csv')
file=csv.reader(data)
header=next(file)
file=list(file)
data.close()
number=input('번호를 입력해주세요:')
cnt=0
over_cnt=0
for row in file:
    if row[-2]!='':
        if datetime.datetime.strptime(row[-2],'%Y-%m-%d')<datetime.datetime.now():
            row[-1]='연체중'
    if number in row[-3]:
        cnt+=1
        if row[-1]=='연체중':
            over_cnt+=1
if over_cnt==0:            
    print('%s번님은 총 %d권을 대출중이고, %d권 대출가능합니다.'%(number,cnt,(5-cnt)))
else:
    print('%s번님은 총 %d권을 대출중이고, 연체중인 도서가 있습니다.'%(number,cnt))
        
while True:
    menu=input('원하시는 메뉴를 선택해주세요\n[메뉴]\n1.대출\n2.반납\n3.종료\n')
    if menu=='1':       #대출
        name=input('대출하실 도서 이름을 입력해주세요:')
        for row in file:
            if name in row[2]:
                if row[-3]!='':
                    print('이미대출중입니다')
                else:
                    row[-4]='대출중'
                    row[-3]=number
                    r_day=datetime.datetime.now()+datetime.timedelta(days=14)
                    row[-2]=r_day.strftime('%Y-%m-%d')
                    print('대출되었습니다')
                    print(header)
                    for row in file:
                        if row[-3]==number:
                            print(row)
                    break
                
    elif menu=='2':       #반납
        name=input('반납하실 도서 이름을 입력해주세요:')
        for row in file:
            if name in row[2]:
                if number in row[-3]:
                    row[-4]=''
                    row[-3]=''
                    print('반납됨')
                    print(header)
                    for row in file:
                        if row[-3]==number:
                            print(row)
                    break
            else:
                print('대출중인 도서가 아닙니다')
                break
    elif menu=='3':       #종료
        break
    else:
        print('다시 입력하세요')
        continue
data=open('book_1.csv','w',newline='')
save=csv.writer(data)
save.writerow(header)
for row in file:
    save.writerow(row)
print('저장되었습니다.')
data.close()
