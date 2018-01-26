from collections import Counter
import matplotlib.pyplot as plt
import csv
경기광주 = csv.reader(open('경기광주.csv'))
경주 = csv.reader(open('경주.csv'))
곤지암 = csv.reader(open('곤지암.csv'))
충주 = csv.reader(open('충주.csv'))
#CSV파일 집합으로 표현하기
경기광주_중복제거 = set()
for item in list(경기광주):
    경기광주_중복제거.add(item[0])
경주_중복제거 = set()
for item in list(경주):
    경주_중복제거.add(item[0])
곤지암_중복제거 = set()
for item in list(곤지암):
    곤지암_중복제거.add(item[0])
충주_중복제거 = set()
for item in list(충주):
    충주_중복제거.add(item[0])    
#전체리스트
전체리스트 = list(경기광주_중복제거) + list(경주_중복제거) + list(곤지암_중복제거) + list(충주_중복제거)
#중복되는 차량의 개수 구하기
통과수 = Counter(전체리스트)
순위1=[]
순위2=[]
순위3=[]
c1=c2=c3=0
for row in 통과수 :
    if 통과수[row] == 4:
        순위1.extend(row+'\n')
        c1 = c1 + 1
    if 통과수[row] == 3:
        순위2.extend(row+'\n')
        c2= c2 + 1
    if 통과수[row] == 2:
        순위3.extend(row+'\n')
        c3 = c3 + 1
        
print("*********** 1순위 차량은 " + str(c1) + "대 ***********")
print(순위1)
print("*********** 2순위차량은 " + str(c2) + "대 ***********")
print(순위2)
print("*********** 3순위차량은 " + str(c3) + "대 ***********")
print(순위3)
    
num = input("강력2팀의 인원수는?")
days = (c1+c2+c3)/(int(num)/2)
print("검거에는 최대" + str(days) + "일 소요된다.")
x = range(4,13)
y = []
for i in x:
    y.append((c1+c2+c3)/(int(i)/2))
plt.rc('font', family= 'Malgun Gothic')
plt.plot(x,y)
plt.title('강력2팀 인원수 대비 검거소요일')
plt.xlabel('인원수')
plt.ylabel('검거소요일')
plt.show()
plt.plot([2,3,4,6],[100,70,50,30],'r')
plt.title('검거소요일 대비 치안만족도')
plt.xlabel('검거소요일')
plt.ylabel('치안만족도')
plt.show() 
