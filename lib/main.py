"""
This is a script to generate a csv file than can be imported into Google Calendar adding all class information
"""
__author__ = 'Anirudh Verma'
__email__ = 'an649hd@gmail.com'
__version__ = '1.0'

from datetime import date
from lib.csv_generator import csv_generator

time_table_location = r'D:\University\Calendar Script\Calendar Script\Files\Timetables\Semester 5 C3.xls'
save_location = r'D:\University\Calendar Script\Calendar Script\Files\CSV Calendar\calendar_csv_C3.csv'

semester_start = date(2019, 8, 5)
semester_end = date(2019, 12, 12)

csv_generator(time_table_location, save_location, semester_start, semester_end)