import matplotlib.pyplot as plt
import numpy as np

S = 50
cl = 1.1
v = np.linspace(0, 30)
rho = 1.225
L = 0.5*rho*v**2*S*cl
L2 = 0.5*rho*v**2*S*0.9

plt.figure()
plt.plot(v, L)
plt.plot(v, L2)
plt.xlabel('Velocity [m/s]')
plt.ylabel('Lift [N]')
plt.show()
