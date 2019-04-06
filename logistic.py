import pandas as pd
import matplotlib.pyplot as plt
d1=pd.read_csv(r"C:\Users\mayank\Downloads\dbm.csv")
x=d1['spend']
gender = {'M': 0.0,'F': 1.0} 
y=d1['sex'].values
y= [gender[item] for item in y] 
import math as m
Xp=[]
for i in x:
    Xp.append(m.exp(i)/(1+m.exp(i)))
Yp=[]
for i in Xp:
    if i < 0.6:
        Yp.append("1.0")
    else:
        Yp.append("0.0")
plt.scatter(Xp,Yp)
plt.show()

plt.scatter(y,x)
plt.show()