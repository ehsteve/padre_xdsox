"""
Tools to analyze and plan the mission in Phase A.
"""
import os

from astropy.time import Time, TimeDelta

from sunpy.net import Fido
from sunpy.net import attrs as a

import xdsox

def get_flarelist():
    """
    Query HEK for flares > C1 from past solar cycle and save results to csv.
    
    """
    event_type = "FL"
    tstart = "2009/01/01"
    tend = "2021/12/31"
    result = Fido.search(
        a.Time(tstart, tend),
        a.hek.EventType(event_type),
        a.hek.OBS.Observatory == "GOES",
        a.hek.FL.GOESCls >= "C1.0",
    )

    new_result = result["hek"][
        "event_starttime", "event_peaktime", "event_endtime", "fl_goescls", "ar_noaanum"
    ]
    return new_result

def update_flarelist():
    """
    Run this to update the flare list.
    """
    result = get_flares()
    filename = os.path.abspath(os.path.join(xdsox._data_directory, ""solar_cycle24_flares.csv"))
    result.write("solar_cycle24_flares.csv", format="csv")

def 

flares_24 = pd.read_csv(os.path.join(_package_directory, "solar_cycle24_flares.csv"))

    def get_class(goes_cls):
        return goes_cls[0]

    flares_24["goes_cls"] = flares_24["fl_goescls"].map(get_class)

    times = parse_time(flares_24["event_starttime"]).datetime
    flares_24["new_times"] = times + relativedelta(years=11)
    flares_24 = flares_24.set_index("new_times")

    flares_24["counts"] = np.ones(len(flares_24))
    flares_24_c = flares_24[flares_24["goes_cls"]=="C"].resample("1M").sum()
    flares_24_m = flares_24[flares_24["goes_cls"]=="M"].resample("1M").sum()
    flares_24_x = flares_24[flares_24["goes_cls"]=="X"].resample("1M").sum()


def get_noaa_indices():

    time_range = TimeRange("2008-06-01 00:00", Time.now())
    result = Fido.search(a.Time(time_range), a.Instrument('noaa-indices'))
    f_noaa_indices = Fido.fetch(result)
    result = Fido.search(a.Time(time_range.end, time_range.end + TimeDelta(4 * u.year)),
                        a.Instrument('noaa-predict'))
    f_noaa_predict = Fido.fetch(result)
    noaa = ts.TimeSeries(f_noaa_indices, source='noaaindices').truncate(time_range)
    noaa_predict = ts.TimeSeries(f_noaa_predict, source='noaapredictindices')

    return noaa, noaa_predict
