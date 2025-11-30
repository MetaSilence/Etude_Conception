# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 16:49:15 2025

@author: nicol
"""
import numpy as np
import matplotlib.pyplot as plt

n = [1.33, 1.5, 2, 3.5]
ln = 0
upwave = 400
lwave = 1400
wavelc = 500

nanoaxis = np.arange(400, 2201, 1)

Q = []
P = [0]
tlmda = []
R = []

def Q_solver (n, i):
    tau = (2 * n[i]) / (n[i]+n[i+1])
    gamma = (n[i] - n[i+1]) / (n[i] + n[i+1])
    Q_new = (1 / tau) * np.array([[1, gamma], [gamma, 1]])
    return Q_new

def P_solver(lmda, central_wav):
    delta = complex(0, (np.pi/2)*(central_wav/lmda))
    P_new = np.array([[np.exp(delta), 0], [0, np.exp(-delta)]])
    return P_new
    

Q.append(Q_solver(n, 0))
Q.append(Q_solver(n, 1))
Q.append(Q_solver(n, 2))

for lmda in range(400, 2201):
    P[0] = P_solver(lmda, 650)
    T = Q[0] @ P[0]
    T = T @ Q[1]
    T = T @ P[0]
    T = T @ Q[2]
    G = abs(T[1][0] / T[0][0])
    R.append(G**2)
    T = 1 - G**2
    tlmda.append(T)
    
plt.plot(nanoaxis, tlmda)
plt.plot(nanoaxis, R)
    


