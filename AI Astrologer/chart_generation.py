from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
import pytz
from datetime import datetime as dt

def get_lat_lon(place_name):

    geolocator = Nominatim(user_agent="ai_astrologer", timeout=5)
    location = geolocator.geocode(place_name)
    if not location:
        raise ValueError(f"Could not find location for {place_name}")
    return location.latitude, location.longitude

def get_timezone(lat, lon):

    tf = TimezoneFinder()
    tz_name = tf.timezone_at(lng=lon, lat=lat)
    if not tz_name:
        raise ValueError("Could not determine timezone.")
    return tz_name


def generate_chart_summary(date_str, time_str, place_name):
    
    print("Getting location coordinates...")
    lat, lon = get_lat_lon(place_name)

    print("Getting timezone...")
    tz_name = get_timezone(lat, lon)
    tz = pytz.timezone(tz_name)

    # Parse date_str (DD/MM/YYYY) and time_str (HH:MM:SS)
    dt_obj = dt.strptime(f"{date_str} {time_str}", "%d/%m/%Y %H:%M:%S")
    utc_offset = dt_obj.astimezone(tz).strftime("%z")  # "+0530"
    utc_offset = utc_offset[:-2] + ":" + utc_offset[-2:]  # format "+05:30"

    date = Datetime(date_str, time_str, utc_offset)
    pos = GeoPos(lat, lon)

    # print("Generating chart...")
    chart = Chart(date, pos)
    sun = chart.get(const.SUN)
    moon = chart.get(const.MOON)
    asc = chart.getAngle(const.ASC)

    summary = f"Sun in {sun.sign}, Moon in {moon.sign}, Ascendant in {asc.sign}. (Timezone: {tz_name})"
    return summary
