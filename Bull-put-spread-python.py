#!/usr/bin/env python
# coding: utf-8

# In[17]:


import numpy as np
import datetime as dt
import scipy as sp
import math as mt
import matplotlib.pyplot as plt


# In[18]:


#parametri di input
S0=4568.02
rf=0.0019
sigma=0.24
n_steps=100
xputITM=5068.02
xputOTM=4068.02
n_simulation=1000 

#calcolo giorni
date1=dt.datetime(2021,12,20)
date2=dt.datetime(2022,1,21)
days=date2-date1
print(days)
T=32/252.0
dt=T/float(n_steps)    


# In[19]:


#seme della distribuzione per calcolo valori aleatori
np.random.seed(12345)  #valori di una distribuzione uniforme



#array dei payoff 500 simulazioni
putOTM=np.zeros([n_simulation], dtype=float)    #array payoff put OTM
putITM=np.zeros([n_simulation], dtype=float)    #array payoff put ITM

x=np.arange(0, int(n_steps), 1)    #range dei passi che va da 0 al numero di steo definito con passo 1


# In[20]:


#definire la funzione della put asiatica otm 

def MC_longOTM(S0, xputOTM, sigma, rf, n_steps, T, dt, n_simulation):  
    for j in range (0, n_simulation):
        ST=S0
        total=0
        for i in np.arange(0,int(n_steps)):
            e=np.random.normal()                                          #definire epsilon 
            ST*=np.exp((rf-0.5*sigma*sigma)*dt+sigma*e*np.sqrt(dt))       #calcolo del sottostante
            total=total+ST                                                #somma cumulata
            price_average=total/n_steps                                   #prezzo medio del sottostante
            putOTM[j]=max(xputOTM-price_average,0)                        #payoff dell'opz per le m simulazioni
    put_priceOTM=np.mean(putOTM)
    return put_priceOTM 


MC_longOTM(4568.02 ,4068.02 ,0.24 ,0.0019 ,100 ,32/252 ,0.001269841 ,500) #payoff put otm


# In[21]:


#definire la funzione per put asiatica itm
def MC_shortITM(S0, xputITM, sigma, rf, n_steps, T, dt, n_simulation):  
    for j in range (0, n_simulation):
        ST=S0
        total=0
        for i in np.arange(0,int(n_steps)):
            e=np.random.normal()
            ST*=np.exp((rf-0.5*sigma*sigma)*dt+sigma*e*np.sqrt(dt))
            total=total+ST
            price_average=total/n_steps
            putITM[j]=max(xputITM-price_average,0)
    put_priceITM=np.mean(putITM)
    return put_priceITM

MC_shortITM(4568.02 ,5068.02 ,0.24 ,0.0019 ,100 ,32/252 ,0.001269841 ,500) #payoff put ITM


# In[22]:


#definire funzione per il calcolo della strategia
def BULL_putspread(S0,xputITM, xputOTM, sigma, rf, n_steps, T, dt, n_simulation):
    POTM= MC_longOTM(S0, xputOTM, sigma, rf, n_steps, T, dt, n_simulation)
    PITM= MC_shortITM(S0, xputITM, sigma, rf, n_steps, T, dt, n_simulation)
    return (POTM-PITM) #acquisto put otm e vendo put itm


# In[23]:


##RISK GRAPH

#array del sottostante 
S1=np.arange(3654.416, 5481.624, 10, float)  

#array della strategia
BULL_SPREAD=np.zeros((len(S1)))


for i in range(0,len(S1)):
    BULL_SPREAD[i]= BULL_putspread(S1[i], xputITM, xputOTM, sigma, rf, n_steps, T, dt, n_simulation)
   
#grafico
plt.plot(S1, BULL_SPREAD) #creo grafico dove x=s1 e y=bullspread
plt.title("BULL_PUT_SPREAD")  
plt.xlabel("SOTTOSTANTE")    
plt.ylabel("PAYOFF")
#plt.xticks(S1)
#plt.yticks(BULL_SPREAD)
plt.show()   


# In[24]:


BULL_putspread(4568.02 ,5068.02 ,4068.02 ,0.24 ,0.0019 ,100 ,32/252 ,0.001269841 ,500 ) #valore del bull spread a scandenza

