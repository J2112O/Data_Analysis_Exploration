#!/usr/bin/python3.6
import csv
import dateutil.parser

# Borrowed and trying these from Data Science Book I had


def parse_rows_with(reader, parsers):
    """wrap a reader to apply the parsers to each of its rows"""
    for row in reader:
        yield parse_row(row, parsers)


def try_or_none(f):
    """wraps f t return None if f raises an exception assumes f takes only one iput"""
    def f_or_none(x):
        try:
            return f(x)
        except:
            return None
    return f_or_none


def parse_row(input_row, parsers):
    return [try_or_none(parser)(value) if parser is not None else value for value, parser in zip(input_row, parsers)]


def cleanup():
    data = []
    with open("trial.csv", "r") as f:
        reader = csv.reader(f)
        #header = next(reader)
        for line in parse_rows_with(reader, [dateutil.parser.parse, None, float]):
            data.append(line)
    # print(header)
    for row in data:
        if any(x is None for x in row):
            print(row)

    '''
    file = ('acs2015_county_data.csv')
    with open(file, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data_set = []
        for row in csv_reader:
            census_id = int(row[0])
            state = str(row[1])
            county = str(row[2])
            total_pop = int(row[3])
            men = int(row[4])
            women = int(row[5])
            hispanic = float(row[6])
            white = float(row[7])
            black = float(row[8])
            native = float(row[9])
            asian = float(row[10])
            pacific = float(row[11])
            citizen = int(row[12])
            income = str(row[13])  # Tried float but wouldn't work.
            income_err = str(row[14])  # Tried float but wouldn't work.
            income_per_cap = int(row[15])
            income_per_cap_err = int(row[16])
            poverty = float(row[17])
            child_poverty = str(row[18])  # Tried float but wouldn't work.
            profession = float(row[19])
            service = float(row[20])
            office = float(row[21])
            construction = float(row[22])
            production = float(row[23])
            drive = float(row[24])
            carpool = float(row[25])
            transit = float(row[26])
            walk = float(row[27])
            other_transp = float(row[28])
            work_at_home = float(row[29])
            mean_commute = float(row[30])
            employed = int(row[31])
            private_work = float(row[32])
            public_work = float(row[33])
            self_employed = float(row[34])
            family_work = float(row[35])
            unemployment = float(row[36])

            data_set.append([census_id, state, county, total_pop, men, women, hispanic, white, black, native, asian, pacific, citizen, income, income_err, income_per_cap, income_per_cap_err, poverty, child_poverty, profession, service, office, construction, production, drive, carpool, transit, walk, other_transp, work_at_home, mean_commute, employed, private_work, public_work, self_employed, family_work, unemployment])

        Saving the work so far until I can get a look at the three columns
        semi_clean_file = ('semi_clean_file.csv')
        file = open(semi_clean_file, 'w')
        writer = csv.writer(file)
        writer.writerow(header)
        for i in range(len(data_set)):
            writer.writerow(data_set[i])

    with open(semi_clean_file, newline='') as file_to_look:
        reader = csv.reader(file_to_look)
        head = next(reader)
        data_to = [row for row in reader]
        print(head)
        print(data_to[0])


def explore_a_csv(some_file):
    file_to_explore = (some_file)
    with open(file_to_explore, newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = [row for row in csv_reader]
        print(header)  # Printing the column names.
        print(data[0])  # Printing the first row of data.
'''


if __name__ == '__main__':
    cleanup()
