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
wav = np.arange(4, 22.001, 0.01)
indexes = np.arange(1, 3.1, 0.1)
nanoaxis = np.arange(400, 2201, 1)  
nanoaxis2 = np.arange(400, 1401, 1)
irrad = (6.16e5 / (wav ** 5 * (np.exp(2484/(wav * 10 ** 2))-1)))

Q = []
P = [0]
tlmda = []
R = []
power = []
reflect = []
row = []
k_value = []
j_value = []

def Q_solver (n, i):
    tau = (2 * n[i]) / (n[i]+n[i+1])
    gamma = (n[i] - n[i+1]) / (n[i] + n[i+1])
    Q_new = (1 / tau) * np.array([[1, gamma], [gamma, 1]])
    return Q_new

def P_solver(lmda, central_wav):
    delta = complex(0, (np.pi/2)*(central_wav/lmda)) #takes into account j
    P_new = np.array([[np.exp(delta), 0], [0, np.exp(-delta)]])
    return P_new

def reflect_solver(n):
    Q.append(Q_solver(n, 0)) #Solver for the matrices outisde of loop
    Q.append(Q_solver(n, 1))
    Q.append(Q_solver(n, 2))
    
    for lmda in range(400, 1401):
        P = [0] #Create first placeholder value
        P[0] = P_solver(lmda, 650) #Solvers for P
        T = Q[0] @ P[0] #Produces de matrix multiplications
        T = T @ Q[1]        
        T = T @ P[0]
        T = T @ Q[2] 
        G = abs(T[1][0] / T[0][0]) #Reflection coefficient definiton
        R.append(G**2) 
        
    T = 0 #Generic memory maintenance
    tlmda.clear()
    Q.clear()
    P.clear()
    return(R)
    
def power_solver(n):
    
    Q.append(Q_solver(n, 0))
    Q.append(Q_solver(n, 1))
    Q.append(Q_solver(n, 2))
    
    for lmda in range(400, 2201):
        P = [0]
        P[0] = P_solver(lmda, 650)
        T = Q[0] @ P[0]
        T = T @ Q[1]        
        T = T @ P[0]
        T = T @ Q[2]        
        G = abs(T[1][0] / T[0][0])
        R.append(G**2)
        T = 1 - G**2
        tlmda.append(T)
        
    wav = np.arange(4, 22.001, 0.01)
    nanoaxis = np.arange(400, 2201, 1)    
    irrad = (6.16e5 / (wav ** 5 * (np.exp(2484/(wav * 10 ** 2))-1)))
    value = np.trapz(tlmda*irrad, nanoaxis)
    T = 0
    tlmda.clear()
    Q.clear()
    P.clear()
    R.clear()
    return value



for k in indexes:
    n = [1.33, 1.5, k, 3.5]
    power.append(power_solver(n))
    
n = [1.33, 1.5, 2.433, 3.5]
reflect.append(reflect_solver(n))
plt.plot(indexes, power)
plt.show()
plt.plot(nanoaxis2, np.transpose(reflect))
plt.xlabel("Longueur d'onde")
plt.ylabel("Réflectivité")
plt.title("Graphique de la réflectivité selon la longueur d'onde")
plt.show()

n = [1.33, 1.5, 2.433, 3.5]
power2 = power_solver(n)
print(power2)

indexes = np.arange(1, 3.1, 0.1)
for k in indexes:
    for j in indexes:
        n = [1.33, k, j, 3.5]
        row.append(power_solver(n))
        j_value.append(j)
        k_value.append(k)
        
value2 = np.trapz(irrad, nanoaxis)
a = max(row)
index_of_maximum = row.index(a)
percent = a/value2 * 100
actualk = k_value[index_of_maximum]
actualj = j_value[index_of_maximum]

print(f"the maximum power output of the system is {a}" )
print(f"The percent of power is {percent}")
print(f"The values of n1 and n2 are {actualk} and {actualj}")

list1 = []
list2 = []

for k in indexes:
    n = [1.333, 1.5, k, 3.5]
    list1.append(power_solver(n)) 

plt.plot(indexes, list1)
plt.xlabel("Index n2")
plt.ylabel("Pouvoir transmis")
plt.title("Graphique de variation de n2 si n1 = 1.5")
plt.show()
    
for j in indexes:
    n = [1.333, j, 2.433, 3.5]
    list2.append(power_solver(n))
    
plt.plot(indexes, list2)
plt.xlabel("Index n1")
plt.ylabel("Pouvoir transmis")
plt.title("Graphique de variation de n1 si n2 = 2.433")
plt.show()

    
        




    
