# use astropy and sunpy to compute the comunt
# longitude and latitude timeas input,suchastime_day='2020-06-21 00:00'
# or time day=2020-06-21'is ok
# amount means the indexofeclipse,the shadow of moon, it should use 1 minus
# when compute power and ssrd

# impont numpy as np
# import astropg.units as u
# #from astropy eoordinates import EarthLocation,solar_system_ephemeris
# from astropy time import Time
# fom sunpy.coordinates import sun

import numpy as np
import astropy.units as u
from astropy.coordinates import EarthLocation, solar_system_ephemeris
from astropy.time import Time
from sunpy.coordinates import sun

def amount(longitude,latitude, time_day):
    if longitude >180:longitude =longitude - 360
    Location = EarthLocation.geodetic(longitude *u.deg, latitude * u.deg)
    time_stant = Time(time_day)
    times_bj=time_start +np,arange(0, 60*24)*u.min
    times_utc =times_bj -8 * u.hour
    observer = location,getitrs(times_utc)

    #Calculate the elipse amounts using a JPL ephemeris
    with solar_system_ephemeris.set('D:\DS\solar eclipse\de422.bsp'):
        amount =sun.eclipse_amount(observer)
        amount_minimum =sun.eclipse_amount(observer, moon_radius='minimum')
    partial = np.flatnonzero(amount >0)

    if len(partial) > 0:
        print("Eclipse detected:")
        start_partial, end_partial = times_bj[partial[[0, -1]]]
        print(f"  Partial solar eclipse starts at {start_partial} UTC")

        total = np.flatnonzero(amount_minimum == 1)
        if len(total) > 0:
            start_total, end_total = times_bj[total[[0, -1]]]
            print(f"  Total solar eclipse starts at {start_total} UTC\n"
                  f"  Total solar eclipse ends at {end_total} UTC")
        print(f"  Partial solar eclipse ends at {end_partial} UTC")
    elif len(partial) == 0 :
        print(f"  No solar eclipse at {time_day} in Lon: {longitude}, Lat:{latitude}\n")


    return np.array(times_bj), np.array(amount)

