import datetime

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d-%m-%Y')

