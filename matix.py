import tensorflow as tf
from numpy import random
import numpy as np	
arr = np.zeros([20,2])
for i in range(20):
    arr[i][0] = i
    arr[i][1] = 2*i + 4 + random.randn(1)
import matplotlib.pyplot as plt
plt.plot(arr[:,0], arr[:,1])
plt.show()
def regression(arrx, arry, mount):
    a = 0
    b = 0
    print(arrx, arry,mount)
    loss_para = 1000
    while(loss_para > 10):
        sum_loss = 0
        x_loss = 0 
        loss_para = 0
        for i in range(len(arrx)):
            sum_loss += a*arrx[i] + b - arry[i]
            x_loss += sum_loss* arrx[i]
	 
        a = a - mount*sum_loss/len(arrx)
        b = b - mount*x_loss/len(arrx)
        for i in range(len(arrx)):
            loss_para += (a*arrx[i] + b - arry[i])**2
        print(loss_para)
        
    print(a,b, loss_para)
            
regression(arr[:,0], arr[:,1], 0.1)  
