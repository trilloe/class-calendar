"""
BUGS
1. Shifts data by one after lunch (FIXED)
   REASON: Reason was that columns f and g, k and l are merged
   FIX: Added logic to ignore these columns
2. For single word locations like FRL, adds teacher's name to location (FIXED)
   FIX: Checks cell A18 and checks if the second entry is in teacher names, if not then location has two words and adds
        both else location is one word and only adds one
"""
import xlrd


def get_data_excel(location):
    workbook = xlrd.open_workbook(location)
    sheet = workbook.sheet_by_index(0)

    data = {}

    for day in range(8, 15):
        data[sheet.cell_value(day, 0)] = []
        for period in range(1, 15):
            if period == 6 or period == 11:
                continue

            if sheet.cell_value(day, period) != '':
                day_data = sheet.cell_value(day, period).split()
                teacher_names = sheet.cell_value(17, 0)

                if day_data[3] not in teacher_names:
                    data[sheet.cell_value(day, 0)].append('%s %s,(%s),%s %s' % (
                        day_data[0],
                        day_data[1].split('-')[0],
                        day_data[1].split('-')[1],
                        day_data[2],
                        day_data[3]
                    ))
                else:
                    data[sheet.cell_value(day, 0)].append('%s %s,(%s),%s' % (
                        day_data[0],
                        day_data[1].split('-')[0],
                        day_data[1].split('-')[1],
                        day_data[2]
                    ))
            else:
                data[sheet.cell_value(day, 0)].append('')

    return data

