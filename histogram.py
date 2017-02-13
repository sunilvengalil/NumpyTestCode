import numpy as np;


a = np.zeros([5,5]);

for i in range(2):
	for j in range(2):
		a[i,j]=1;

print a;
print np.histogram(a);