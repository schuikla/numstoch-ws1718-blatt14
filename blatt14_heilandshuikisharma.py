# -*- coding: utf-8 -*-
"""
exercise sheet 14, ex2
@author: Ibrahim Eraslan, 3239441 
@author: Alexander Fischer, 3227877 
@author: Rene Richard Tischler, 3261464 
"""
import math


def f(t):
	global counter
	counter += 1
	return (1/math.sqrt(2*math.pi)) * math.exp((-t*t) / 2)

def phii(t):
	global counter
	counter += 1
	return (1/math.sqrt(2*math.pi)) * math.exp((-t*t) / 2)

def simpson(a, b, N):
	res = 0
	h = (b - a) / N
	for i in range(N):
		res += 2*f(a+i*h) + 4*f(a+i*h+h/2)
	res -= f(a)
	res += f(b)
	return res*(h/6) + 0.5 #-0.95



## 2a)
#b = 1
#for i in range(10,31):
#	counter = 0
#	e = 2**-i
#	n = 1
#	while True:
#		if abs(simpson(0,b,n) - simpson(0,b,2*n)) < e:
#			n = 2*n
#			break
#		else:
#			n = 2*n
#	res = simpson(0,b,n) - 0.84134474606854293
#	print("ε = 2^(-" + str(i) + "): ", "\n\t approximation: ", "%.25f" % (res + 0.84134474606854293) , "  \n\t error:" ,"%.50f" % res, "\n\t Auswertungen: ", counter,'\n')



# 2b)

for i in range(10,31):
	e = 2**-i
	u = 0
	counter = 0
	countnewton = 0
	while True:
		countnewton += 1
		
		n = 1
		while True:
			if abs(simpson(0,u,n) - simpson(0,u,2*n)) < e/10:
				n = 2*n
				break
			else:
				n = 2*n
		simp = simpson(0,u,n)
		diff = abs(simp)
		if diff < e:
			print("ε = 2^(-" + str(i) + "): ", "\n\t u =", "%.20f" % u, "\n\t difference:", "%.30f" % diff, "\n\t Newton iterations:", countnewton, "\n\t Auswertungen:", counter)
			break
		else:
			u = u - simp/phii(u)

