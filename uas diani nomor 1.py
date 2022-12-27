#from sklearn import svm
from sklearn.svm import SVR
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Database
FileDB = 'database uas.txt'
Database = pd.read_csv(FileDB, sep=",", header=0)
print ("---------------------")
print (Database)
#x = data, y = target
x = Database[['a,b,hasil']]
y = Database.hasil
#Fit model regresi
svr_rbf = SVR(kernel='rbf', C=100, gamma=0.1, epsilon=.1)
svr_rbf.fit(x, y)
#Menampilkan data prediksi
xx = np.arange(1, 21, 1)
n = len (xx)
print ("---------------------")
print ("----Prediksi SVM-----")
print ("xx(i) rbf")
for i in range (n):
    rbf = svr_rbf.predict([[xx[i]]])
    print ('{:.2f}'.format(xx[i]), rbf)
print ("---------------------")

