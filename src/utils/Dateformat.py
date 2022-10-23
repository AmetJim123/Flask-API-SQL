import datetime


class Dateformat:

    @classmethod
    def convert_date(self, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y')
