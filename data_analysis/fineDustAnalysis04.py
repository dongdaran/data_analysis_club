#### 4번째 #######
import csv

f = open('STCS_부유분진 농도.csv')
data = csv.reader(f)

result = []

next(data)
data= list(data)
pivot = []

for row in data:
    if '서울' in row[0]:
        for i in range(2, len(row)):
            pivot.append(float(row[i]) / float(row[1]))

            
#mn = 10000000
mn = 1

for row in data:
    s = 0
    for i in range(2, len(row)):
        tmp = float(row[i]) - pivot[i-2]
        s = s+ tmp
    if s < mn :
        result = []
        for i in range(2, len(row)) :
            result.append(float(row[i]) / float(row[1]))

# 차트
import matplotlib.pyplot as plt	
plt.plot(pivot)
plt.plot(result)
plt.show()
