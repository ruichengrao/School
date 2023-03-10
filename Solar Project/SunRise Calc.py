from datetime import date
from suntime import Sun, SunTimeException
from geopy.geocoders import Nominatim
import datetime



 
#getting lon/lat 
geolocator = Nominatim(user_agent="Solar Tracker")
location = geolocator.geocode("201 Walt Banks Rd, Peachtree City, GA 30269")
global lat
lat = location.latitude
global lon
lon = location.longitude



latitude = lat
longitude = lon

sun = Sun(latitude, longitude)

# date object of today's date
today = date.today()
 
year = today.year
month = today.month
day = today.day

# On a special date in your machine's local time zone
abd = datetime.date(year, month, day)
abd_sr = sun.get_local_sunrise_time(abd)
abd_ss = sun.get_local_sunset_time(abd)
print(abd_sr)
