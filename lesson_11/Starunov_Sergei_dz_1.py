import re


class IncorrectDate(Exception):
    pass


class Date:
    __DATE: str
    __regex = re.compile(r'(\d{2})\.(\d{2})\.(\d{4})$')

    def __init__(self, date):  # format date ==> 'dd.mm.YYYY'
        Date.__DATE = date

    @classmethod
    def get_day_month_year(cls):
        if not cls.valid_date(cls.__DATE):
            raise IncorrectDate('Некорректная дата')
        day, month, year = map(int, cls.__DATE.split('.'))
        return day, month, year

    @staticmethod
    def valid_date(date):
        try:
            day, month, year = map(int, Date.__regex.search(date).groups())
        except AttributeError:
            return False
        if (day > 31) or (month < 1 or month > 12) or (month in [4, 6, 9, 11] and day > 30):
            return False
        if not year % 4 and year % 100 or not year % 400:  # Високосный
            if month == 2 and day > 29:
                return False
        else:
            if month == 2 and day > 28:
                return False
        return True


if __name__ == '__main__':
    date = Date('28.02.2001')
    day, month, year = Date.get_day_month_year()
    print(day, month, year)
