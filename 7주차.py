# -*- coding: utf-8 -*-
"""7주차.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MoZUECNj2zBa23vR4NTjO-91OGaZ_wJE
"""

#sort 오름차순
temps= [28,31,33,35,27,26,25]
temps.sort()
print(temps)





#sort 내림차
temps= [28,31,33,35,27,26,25]
temps.sort(reverse=True)
print(temps)

#random
import random
temps= [28,31,33,35,27,26,25]
print(f'랜덤하게 선택한 항목 = {random.choice(temps)}')
colors=['red','green','blue']
print(f'랜덤하게 선택한 항목 = {random.choice(colors)}')

#ex2
scores = [10.0,9.0,8.3,7.5,5.0,9.2,6.4]
print(f'최대값과 최소값 제거 전 : {scores}')

scores.remove(max(scores))
scores.remove(min(scores))

print(f'최대값과 최소값 제거 후: {scores}')

"""빈칸채우기, 코드 결과 추측하기, 코드 작성하기
10시 수업 시작, 자리 맘대로
30분동안 시험볼 예정.
"""

#exercise2
myList=[5,10,15,20,25,30]
print(f'항목 변경 전: myLIst : {myList}')
if 10 in myList:
  myList[myList.index(10)]=100


print(f'항목 변경 후 myList : { myList}')

#exercise 3

#tuple
contry=('korea'),
print(type(contry))
city='seoul',
print(type(city))
month='jan'
print(type(month))
contry2=('korea',)
print(type(contry2))

#EXample1
cityList=['seoul','busan','jeju']
cityTuple=tuple(cityList)
print(cityTuple)
print(type(cityTuple))

countryTuple=('korea','china','japan')
countryList = list (countryTuple)
print(countryList)
print(type(countryList))

#example2

cityList=['seoul','busan','jeju','youngin']
c1,c2,*c3=cityList

print(f'c1={c1},c2={c2},c3={c3}')
student = ('Alex',[90,100,95])
name, scores=student
print(f'student = {student}')
print(f'name = {name}')
print(f'scores = {scores}')

my_list=[1,2,3,4]
result=list(map(lambda x:x*2,my_list))
print(result)



temps=[28,31,33,35,27]
temps[5]=29

rgbColor=['red','blue']
rgbColors=['greeen']
print(f"green exist? : {'greeen' in rgbColor}")
print(f"green exist? : {'greeen' in rgbColors}")

temps=[28,31,33,35,27]
temps.append(36)
for i in range(len(temps)):
  print(f'temps[{i}]={temps[i]}')