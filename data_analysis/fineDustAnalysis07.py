#### 7번째 ######
import csv

f = open('STCS_부유분진 농도.csv')
data = csv.reader(f)

result = []

next(data)
next(data)
data= list(data)
pivot = []

for row in data:
    if '서울' in row[0]:
        for i in range(3, len(row)):
            pivot.append(float(row[i]) / float(row[2]))

            
mn = 1

for row in data:
    s = 0
    for i in range(3, len(row)):
        row[i] = float(row[i]) / float(row[2])
        tmp = (row[i] - pivot[i-3])**2
        s = s + tmp
    if s < mn and ('서울' not in row[0]) :
        result = []
        for i in range(3, len(row)) :
            result.append(float(row[i]))
        mn = s
        

# 차트
import matplotlib.pyplot as plt	
plt.plot(pivot)
plt.plot(result)
plt.show()

