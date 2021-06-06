from datetime import date, datetime, timedelta, time
import re


# Monday - 0
# Tuesday - 1
# Wednesday - 2
# Thursday - 3
# Friday - 4
# Saturday - 5
# Sunday -6


def get_current_date():
    return date.today()


def get_current_datetime():
    return datetime.today()


def get_current_day_of_week():
    return datetime.today().weekday()


def convert_timestamp_to_UTC(timestamp):
    return datetime.fromtimestamp(timestamp)


def convert_UTC_to_timestamp(date):
    return datetime.timestamp(date)


def get_day_of_week_number(day):
    if day == 'dziś' or day == 'dzisiaj':
        return get_current_day_of_week()
    if day == 'poniedziałek':
        return 0
    elif day == 'wtorek':
        return 1
    elif day == 'środa':
        return 2
    elif day == 'czwartek':
        return 3
    elif day == 'piątek':
        return 4
    elif day == 'sobota':
        return 5
    elif day == 'niedziela':
        return 6


def get_time_from_hours_minutes(hours, minutes):
    return time(hours, minutes, 0)


def get_datetime_from_day(day, hours, minutes):
    current_day_of_week = get_current_day_of_week()
    input_date_of_week = get_day_of_week_number(day)
    input_time = get_time_from_hours_minutes(hours, minutes)

    # data wypada na dzisiaj i trzeba sprawdzić godziny
    if current_day_of_week == input_date_of_week:

        #  Podanej czas już był
        if input_time < datetime.now().time():
            date = get_current_date() + timedelta(days=7)
            return datetime.combine(date, input_time)
        # Podana czas jeszcze nie był
        else:
            date = get_current_date()
            return datetime.combine(date, input_time)

    # data będzie z przyszłośći
    else:
        date = get_current_date() + timedelta(days=(7 - abs(current_day_of_week-input_date_of_week)))
        return datetime.combine(date, input_time)


def get_date(date, time):
    # parsowanie czasu
    if re.match(r'^[0-2][0-9]$', time):
        hours = int(time)
        minutes = 00
    elif re.match(r'^[0-2][0-9].[0-9][0-9]$', time):
        m = re.search(r'^([0-2][0-9]).([0-9][0-9])$', time)
        hours = int(m.group(1))
        minutes = int(m.group(2))


# TODO jeżeli jeszcze jakieś dziwne formaty to obsłużyć przypadki
    if re.match(r'^[0-3][0-9]\.[0-1][0-9]\.20[0-9]{2}$', date):
        date = datetime.strptime(date, '%d.%m.%Y').date()
        return datetime.combine(date, get_time_from_hours_minutes(hours, minutes))
    else:
        return get_datetime_from_day(date, hours, minutes)


# Tests
# print(get_datetime_from_day('niedziela', 22, 21))
# print(get_datetime_from_day('niedziela', 18, 21))
# print(get_datetime_from_day('poniedziałek', 18, 21))
# print(get_datetime_from_day('wtorek', 18, 21))

# print(get_date("07.06.2021", "12:00"))
# print(get_date("sobota", "00:00"))
# print(get_date("wtorek", "12:00"))
# print(get_date("12.06.2021", "23"))
