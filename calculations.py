import numpy as np
import matplotlib.pyplot as plt
from fitpeak import fitpeak

data = np.loadtxt('spectrum1021.txt', comments='%')

# manually identified
ranges = [
    [1160, 1280],
    [1287, 1387],
    [3509, 3614],
    [3625, 3703],
]

res = [[*fitpeak(rangemin, rangemax, data[:, 0], data[:, 1])] for rangemin, rangemax in ranges]
peaks_list = [r[0] for r in res]
peaks = np.array(peaks_list)
fits = [r[1] for r in res]
fitranges = [r[2] for r in res]

es = np.array([0,0,0,0]) # actually find these
[m, c] = np.polyfit(peaks[:3], es[:3], 1)

ch = data[:, 0]
e = m*ch + c

fig, ((ax_fit, _), _) = plt.subplots(2, 2)

ax_fit.plot(data[:, 0], data[:, 1])
for peak, f, r in zip(peaks_list, fits, fitranges):
    ax_fit.plot(r, f, 'r')
    ax_fit.text(r[-1], np.max(f), 'ch = %6.1f' % peak)
# ax.plot(e, data[:, 1])
# ax.set_yscale('log')
ax_fit.set_xlabel('Energy (channel)')
ax_fit.set_ylabel('Counts')
ax_fit.set_title('Fit peaks')

plt.show()
