"""
BUGS
1. For multiple back to back classes of same type, create unique entry per class
"""
from datetime import timedelta
from lib.extract__data_excel import get_data_excel


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


def csv_generator(excel_file_location, save_location, semester_start, semester_end):
    csv_data = 'Subject,' \
               'Start Date,' \
               'Start Time,' \
               'End Date,' \
               'End Time,' \
               'All Day Event,' \
               'Description,' \
               'Location,' \
               'Private\n'

    start_time = timedelta(hours=8, minutes=30)

    data = get_data_excel(excel_file_location)

    description = {'CS 332': 'Compiler Design',
                   'CS 4101': 'Linear & Non-Linear Optimisation',
                   'EL 302': 'Digital Image Processing',
                   'CS 261': 'Computer Networks',
                   'CS 301': 'Software Engineering',
                   'FIN 212': 'Indian Finance System',
                   'CS 4221': 'Cloud Services and Technology'
                   }

    for single_date in date_range(semester_start, semester_end):
        day_name = single_date.strftime('%A')[0:3].upper()

        for period in range(11):
            if data[day_name][period] != '':
                class_data = data[day_name][period].split(',')

                csv_data += '%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (
                    '%s %s' % (class_data[0], class_data[1]),
                    single_date,
                    start_time + timedelta(hours=period),
                    single_date,
                    start_time + timedelta(hours=period + 1),
                    'FALSE',
                    description[class_data[0]],
                    class_data[2],
                    'FALSE'
                )

    csv_file = open(save_location, 'w')
    csv_file.writelines(csv_data)
    csv_file.close()

