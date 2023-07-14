import scipy
import scipy.stats as stats
import math
import statistics
n1 = int(input('n1=' ))
n2 = int(input('n2=' ))
table = float(input('TABLE = '))
j = 500
x = input('x=' )
myarr = x.split(" ")
print(x)
for i in range(len(myarr)):
 myarr[i] = float(myarr[i])
print(myarr)
x_bar = sum(myarr)/len(myarr)
print('x_bar =' ,x_bar)
y = input('y=' )
myare = y.split(" ")
print(y)
for l in range(len(myare)):
 myare[l] = float(myare[l])
print(myare)
y_bar = sum(myare)/len(myare)
print('y_bar =' ,y_bar)
j = 501
s1 = float(input('s1='))
s2 = float(input('s2='))
s1 = int(s1)
s2 = int(s2)
if len(x) <j:
 z1 = ((x_bar - y_bar)/math.sqrt(((s1*2)/n1)+((s2*2)/n2)))
 print(z1,'z claculated value')
else :
 z2 = ((x_bar - y_bar)/math.sqrt(((s1*21)/n1)+((s2*2)/n2)))
 print(z2,'z claculated value')
if z1 < table:
 print('accept null hypothsis')
else:
 print('reject null hypothsis')