import numpy as np
import matplotlib.pyplot as plt

n = np.arange(200)
Tb = 1
A = 1
fc = 6
dt =0.005
t = np.arange(0, Tb, dt)
s = A * np.sin(2 * np.pi * fc * t)
#plt.figure(1)
#plt.subplot(2, 1, 1)
#plt.plot(n, s)
#plt.title('s(n)')

sigma2 = 25

c00, c11, c01, c10 =0, 0, 2, 1
PH1 = 0.6
PH0 = 1 - PH1
door1 = (c10 - c00) * PH0 / ((c01 - c11) * PH1)
door2 = 2 / 3

M = 1000
a1 = np.zeros([M])
b1 = np.zeros([M])

for m in range(M):
    n1 = np.sqrt(sigma2) * np.random.randn(200)
    #plt.subplot(2, 1, 2)
    #plt.plot(n, n1)
    #plt.title('noise')
    x11 = s + n1
    x10 = n1
    #plt.figure(2)
    #plt.subplot(2, 1, 1)
    #plt.plot(n, x11)
    #plt.title('x1(t)')
    #plt.subplot(2, 1, 2)
    #plt.plot(n, x10)
    #plt.title('x0(t)')
    #plt.show()
    y11 = np.sum(x11 * s)
    y10 = np.sum(x10 * s)
    es = np.sum(s * s)
    gama1 = sigma2 * np.log(door1) + 0.5 * es
    a1[m] = 1 if y11 > gama1 else 0
    b1[m] = 1 if y10 > gama1 else 0

pd1 = np.sum(a1) / M
pm1 = 1 - np.sum(a1) / M
pf1 = np.sum(b1) / M
risk1 = c00 * (1 - pf1) + c10 * pf1 + c01 * pm1 + c11 * pd1

print('pd1:{:.3f}'.format(pd1))
print('pm1:{:.3f}'.format(pm1))
print('risk1:{:.3f}'.format(risk1))

a2 = np.zeros([M])
b2 = np.zeros([M])
for m in range(M):
    n2 = np.sqrt(sigma2) * np.random.randn(200)
    x21 = s + n2
    x20 = n2
    y21 = np.sum(x21 * s)
    y20 = np.sum(x20 * s)
    es = np.sum(s * s)
    gama1 = sigma2 * np.log(door2) + 0.5 * es
    a2[m] = 1 if y21 > gama1 else 0
    b2[m] = 1 if y20 > gama1 else 0

pd2 = np.sum(a2) / M
pm2 = 1 - np.sum(a2) / M
pf2 = np.sum(b2) / M
risk2 = c00 * (1 - pf2) + c10 * pf2 + c01 * pm2 + c11 * pd2

print('pd2:{:.3f}'.format(pd2))
print('pm2:{:.3f}'.format(pm2))
print('risk2:{:.3f}'.format(risk2))