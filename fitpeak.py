import numpy as np

def fitpeak(minpoint, maxpoint, X, Y):
    Range = np.logical_and(X > minpoint, X < maxpoint)
    xi = X[Range]
    yi = Y[Range]
    l = np.polyfit(xi, np.log(yi), 2)
    [la, lb, lc] = l

    lx0= -lb / (2 * lc)
    lo= la - lc * lx0**2;
    
    mid = lx0

    fit = np.exp(lc * xi**2 + lb * xi + la)
    return mid, fit, xi
