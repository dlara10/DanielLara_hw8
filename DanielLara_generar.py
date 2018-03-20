import numpy as num
import matplotlib.pyplot as plt
import random
#Probabilidad de 
s = [-10,-5,3,9] 
h = [0.1,0.4,0.2,0.3]
#funcion para calcular las probabilidades
def sample_1(N):
	x = []
	x.append(num.random.choice(a = s,size = N,p =h))
	return x


#Funcion para calcular probabilidad exponencial
def sample_2(N):
	x = []
	x.append(num.random.exponential(scale = 0.5, size = N))
	return x

#Funcion para retornan M promedios
def get_mean(sampling_fun, N, M):
	x = 0
	y = []
	for i in range(M):
		x = num.mean(sampling_fun(N))
		y.append(x)
	return y
N = [10.0, 100.0, 1000.0]
for i in (N):
	x = 0
	y = 0
	x = get_mean(sample_1, i, 10000)
	y = get_mean(sample_2, i, 10000)
	if(i == 10.0):
		num.savetxt("sample_1_10.txt", x)
		num.savetxt("sample_2_10.txt", y)
	elif(i == 100.0):
		num.savetxt("sample_1_100.txt", x)
		num.savetxt("sample_2_100.txt", y)
	else:
		num.savetxt("sample_1_1000.txt", x)
		num.savetxt("sample_2_1000.txt", y)
	
		
		



	
