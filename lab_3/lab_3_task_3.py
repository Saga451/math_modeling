import numpy as np 
from lab_3_task_1 import g

v0 = int(input("Type the start velocity: "))
a = float(input("Type the angle of the throw: pi * "))

vx0 = np.cos(np.pi * a) * v0 
vy0 = np.sin(np.pi * a) * v0

for t in np.arange(0, 100, 0.2):

    x = vx0 * t
    y = vy0 * t - (g * (t ** 2)) / 2
    
    x1 = x // 1
    y1 = y // 1
    
    if y <= 0  and t != 0:
        break

    tb = [t, x1, y1]
    print(tb)
