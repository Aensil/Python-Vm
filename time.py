import datetime

the_time = datetime.datetime.now()  #fecha y hora
the_hour = datetime.date.today()    #Fechas

#the_year = print(the_hour.year())
#print(f'Year:{the_hour.year()}')
#the_month = the_hour.month()
#the_day = the_hour.day() 
''''
%Y  = Year
%m  = Month
%d  = Day
%H  = Hour
%M  = Minute
%S  = Second
''' 
from datetime import datetime
the_date = the_time.strftime('%d/%m/%Y')
print(f'Latam: {the_date}')
print(the_time)

#pip install pytz
import pytz
#https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))