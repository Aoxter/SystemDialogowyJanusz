from datetime import date, datetime, timedelta, time

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

        # print(get_current_datetime('niedziela', 22, 21))
print(get_datetime_from_day('niedziela', 22, 21))
print(get_datetime_from_day('niedziela', 18, 21))
print(get_datetime_from_day('poniedziałek', 18, 21))
print(get_datetime_from_day('wtorek', 18, 21))
