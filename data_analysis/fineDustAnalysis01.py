#### 1번째 #######
import csv

f = open('STCS_부유분진 농도.csv')
data = csv.reader(f)

result =[]
for row in data:
    if '서울'in row[0]:
        for i in range(1,len(row)):
            result.append(float(row[i]))

#print(result)

# 차트
import matplotlib.pyplot as plt	
plt.plot(result)
plt.show()
