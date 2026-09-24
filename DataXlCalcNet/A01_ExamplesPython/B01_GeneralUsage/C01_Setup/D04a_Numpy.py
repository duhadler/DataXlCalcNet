
import numpy as np
from xlcalcnet import dpm
    

def demo_mp():
    r = 8
    c = 2
    dpm.dps = 30
    R = np.ndarray((r,c),dtype=dpm.realtype)
    d1 = dpm.t(1.0)
    for i in range(r):
        for j in range(c):
            R[i,j] = 10*(i+1) + d1/(j+7)
    print(R)
    print()
    res = np.mean(R)
    print("res = np.mean(R): \n", res, type(res))
    print()
    res = np.mean(R, axis=0)
    print("res = np.mean(R, axis=0): \n", res, type(res))
    print()
    res = np.mean(R, axis=1)
    print("res = np.mean(R, axis=1): \n", res, type(res))



def demo_all():
    demo_mp()

demo_all()




