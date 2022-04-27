import numpy as np
import matplotlib.pyplot as plt
from fitpeak import fitpeak

data = np.loadtxt('spectrum1021.txt', comments='%')

# manually identified
ranges = [
    [1310, 1357], # E2
    [3529, 3584], # E3
    [3639, 3686], # E4
]

res = [[*fitpeak(rangemin, rangemax, data[:, 0], data[:, 1])] for rangemin, rangemax in ranges]
peaks_list = [r[0] for r in res]
peaks = np.array(peaks_list)
fits = [r[1] for r in res]
fitranges = [r[2] for r in res]

# MeV
es = np.array([
    1.0101, # E2
    2.6694, # E3
    2.7492, # E4
]) 
[m, c] = np.polyfit(peaks, es, 1)

ch = data[:, 0]
e = m*ch + c
print(m, c)

E_min, E_max = 0.913, 0.947
E1_peak, E1_fit, E1_fitrange = fitpeak(E_min, E_max, e, data[:, 1])

non_zero_count = data[:, 1] > 0.0
Q = e[non_zero_count][-1]

fig, (ax_fit, ax_calib) = plt.subplots(1,2)

ax_fit.plot(data[:, 0][non_zero_count], data[:, 1][non_zero_count], lw=1.0)
for i, (peak, f, r) in enumerate(zip(peaks_list, fits, fitranges)):
    ax_fit.plot(r, f, 'r', lw=1.0)
    ax_fit.text(r[-1], np.max(f), 'E%1d(ch=%6.1f)' % (i+2, peak))
ax_fit.set_xlabel('Energy (channel)')
ax_fit.set_ylabel('Counts')
ax_fit.set_title('Fit peaks E2-E4')


ax_calib.plot(e[non_zero_count], data[:, 1][non_zero_count], lw=1.0)
ax_calib.plot(E1_fitrange, E1_fit, 'r', lw=1.0)
ax_calib.text(E1_fitrange[-1], np.max(E1_fit), 'E1=%5.3f MeV' % E1_peak)
ax_calib.text(Q, 250, 'Q = %4.2f MeV' % Q, ha='center')
ax_calib.set_xlabel('Energy (MeV)')
ax_calib.set_ylabel('Counts')
ax_calib.set_title('Calibrated Spectrum and E1 peak')

fig.suptitle('$^{10+21}$St Calibration')
plt.show()

