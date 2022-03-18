"""
Estimate number of flares we can expect to see
"""

import datetime
import matplotlib.pyplot as plt
import pandas as pd

from sunpy.time import parse_time

from xdsox.phasea import *


fig, ax = plt.subplots(figsize=(10, 7))

ax.axvspan(dates.date2num(parse_time("2021-11-01").datetime), 
        dates.date2num(parse_time("2027-01-01").datetime), 
        alpha=0.1, label="SO/STIX Observations", color="tab:olive", zorder=0)

ax.axvline(misolfa_start - relativedelta(months=1), color="r", 
        label="PADRE Launch")

ax.axvspan(dates.date2num(misolfa_start), 
        dates.date2num(misolfa_end), 
        color="grey", alpha=0.5, zorder=0, 
        label="PADRE Phase E")

ax2 = ax.twinx()
ax2.plot(noaa.index, noaa.quantity('sunspot RI'), label='Sunspot Number')
ax2.plot(noaa_predict.index, noaa_predict.quantity('sunspot'),
        color='grey', label='Near-term Prediction')
ax2.fill_between(noaa_predict.index, noaa_predict.quantity('sunspot low'),
                noaa_predict.quantity('sunspot high'), alpha=0.1, color='grey')
ax2.set_ylabel("Sunspot Number")
ax2.set_ylim(0)

ax.fill_between(flares_24_c.index, flares_24_c["counts"]+flares_24_m["counts"]+flares_24_x["counts"], 
                step="mid", 
                color="tab:green", 
                label="X flares")

ax.fill_between(flares_24_c.index, flares_24_c["counts"]+flares_24_m["counts"], 
                step="mid", 
                color="tab:orange", 
                label="M flares")

ax.fill_between(flares_24_c.index, flares_24_c["counts"], 
                step="mid", 
                color="tab:blue", 
                label="C flares")
ax.grid(False)
ax2.grid(False)

ax.set_xlim(parse_time("2021-01-01").datetime, parse_time("2027-01-01").datetime)
ax.set_ylim(0, 300)
ax.xaxis.set_minor_locator(dates.MonthLocator(interval=2))
ax.legend(loc="upper left")

ax.set_xlabel("Time")
ax.set_ylabel("No. Flares")

plt.savefig('fig6_solar_cycle.pdf')
plt.show()

energy = u.Quantity(np.arange(1, 1000), 'keV')
y = u.Quantity(np.arange(1, 1000), 'keV')

plt.plot(energy, y)
plt.yscale('log')
plt.xscale('log')
plt.xlabel('Energy [' + str(energy.unit) + ']')
plt.show()
