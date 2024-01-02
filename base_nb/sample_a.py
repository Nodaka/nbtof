for nbtof_test_b in range(1,10):
    nbtof_test_c = 4
    for i in range(4,6):
        nbtof_test_d = i
        print(nbtof_test_d, nbtof_test_c)
for i, j in enumerate(range(1,10)):
    nbtof_test_c = 4

instnat_num = 1
while True:
    if instnat_num>5:
        kk=3
        break
    instnat_num = instnat_num + 1
def concat_dum():
    return None
import matplotlib.pyplot as plt
import numpy as np, pandas as pd, random
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from sklearn.gaussian_process.kernels import ConstantKernel, RBF, WhiteKernel
nbtof_test_a, nbtof_test_b = 1,2
nbtof_test_c, nbtof_test_d = 3,4

def sample_a(
    x,
    y,
    d,
    *params,
    deg_for_fit=4,
    **kwargs,
    ):
    """
    fdhjafsl
    """
    
    def fit_func(get_x, *params):
        return_y = np.zeros_like(get_x)
        for i, param in enumerate(params):
            return_y = return_y + np.array(param*get_x**i)
        return return_y
    
    popt, pcov = curve_fit(fit_func, x, y, p0=list(np.ones(deg_for_fit+1)))
    
    check_y = fit_func(x, *popt)

    return check_y
