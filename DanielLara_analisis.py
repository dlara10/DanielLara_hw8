import numpy as num
import matplotlib.pyplot as plt

def normal_dist(x, mean, sigma):
	y = []
	y.append(num.random.normal(loc = mean, scale = sigma))
	return y

def get_fit(filename):
	s = filename
	x = num.histogram(s)
	plt.hist(x)
	plt.savefig("Histograma.png")


