# -*- coding: utf-8 -*-
"""
Blatt 14, Aufgabe 2

Created on Tue Jan 30 12:04:28 2018

@author: lukas
"""
import numpy as np


def calcSimpsonSum(a,b,N):
         h = (b-a)/N
         # Phi(0) =  0.5
         sum = 0
         counter = 0
        
         t_i = np.zeros(N+1)
        
        
         for i in range (0,N+1):
            t_i[i] = a + i*h
            
            if i == 0:
                sum += 1/(np.sqrt(2*np.pi)) * np.e**(-t_i[i]**2 * 0.5) + 4 * np.e**((-t_i[i]+t_i[i+1])**2/2 *0.5)
            elif i == N:
                sum += 1/(np.sqrt(2*np.pi)) * np.e**(-t_i[i]**2 * 0.5)
            else:
                sum += 1/(np.sqrt(2*np.pi)) * np.e**(-t_i[i]**2 * 0.5)
                
            counter += 1
        #end of for
        
         sum *= h
         sum += 0.5
         results = [sum, counter]
         return results
    
     
def finalCalculation(a,b,epsilon, param):
    exactValue = 0.84134474606854293
    s1 = 1
    s2 = 0
    diff = s1-s2
    n = 2**param
    
    while diff >= epsilon:
        s1 = calcSimpsonSum(a,b,n)
        s2 = calcSimpsonSum(a,b,2*n)
        diff = np.abs(s1[0] -s2[0])
        n *= 2
    
    result = [s2[0], s2[0]-exactValue, s2[1], n/2]
    print('n:', n/2)
    return result
    
#    print('simpson sum: ' + str(s2[0]))
#    print('error: ' + str(s2[0]-exactValue))
#    print('function calls: ' + str(s2[1]))


#############################################
################# Main ######################
#############################################

for i in np.arange(10,31):
    print('epsilon = 2**(', -i , ')')
    result = finalCalculation(0,1,1/(2**i), i+2)
    print('simpson sum:', result[0])
    print('error:', result[1])
    print('function calls:', result[2])
    print('')
        
    
    
    
    
    
    
    
    