import csv

class TT_tesdata:

    login = "Admin"

    password = "admin123"

    data_file = "PersonalProjectWork\DEMO_HRM\data_file.csv"

    def get_dataCSV(filename):
        rows = []
        datafile = open(filename, "r")
        reader = csv.reader(datafile)
        next(reader, None)
        for row in reader:
            rows.append(row)
        return rows