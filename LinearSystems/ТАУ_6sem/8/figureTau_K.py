
import matplotlib.pylab as plt
import numpy as np
import math as m

def devision(a):
    return a/1000

def TauCalculate(k):
    w = (k**2 - 1)**0.5
    psi = m.atan2(w,4) - m.atan2(5*w,(4 - w**2))
    return (psi + m.pi)/w

K = list(map(devision, range(1001,5000)))
Tau1 = []
zero = []
for k in K:
    Tau1.append(TauCalculate(k))
    zero.append(0)

plt.plot(K,Tau1)
plt.plot(K,zero)
plt.ylabel("Критическая задержка [с]")
plt.xlabel("Коэффициент усиления")
plt.show()

