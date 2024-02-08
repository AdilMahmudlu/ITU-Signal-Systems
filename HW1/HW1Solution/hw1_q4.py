import numpy as np
import matplotlib.pyplot as plt

    
t = np.arange(-100,100,0.1)
n = np.arange(-100,101)

def impulse(x):
    return 1*(x == 0)

def step(x):
    return 1*(x >= 0)

def stepDiscrete(x):
    return 1*(np.logical_and(x >= 0, np.remainder(x, 1) == 0))

x1 = lambda t: step(t+4) - step(t-4) + step(t+3) - step(t-3) + step(t+1) - step(t-1)
x2 = lambda n: stepDiscrete(n+4) - stepDiscrete(n-4) + stepDiscrete(n+3) - stepDiscrete(n-3) + stepDiscrete(n+1) - stepDiscrete(n-1)

y1 = x1(t/2) + x1(2*t)

y2 = np.zeros(t.shape)
for k in range(1,21,1):
    y2 += x1(t/k)

y3 = x2(1/2*n) + x2(2*n)

y4 = np.zeros(n.shape)
for k in range(1,21,1):
    y4 += x2(n/k)


plt.plot(t, y1)
plt.savefig('q4_y1.png')
plt.close()

plt.plot(t, y2)
plt.savefig('q4_y2.png')
plt.close()

plt.stem(n, y3)
plt.savefig('q4_y3.png')
plt.close()

plt.stem(n, y4)
plt.savefig('q4_y4.png')
plt.close()