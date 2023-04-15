from datetime import datetime

MIN_IN_H = 60
SEC_IN_MIN = 60
DAY_IN_WEEK = 7


def get_time_left_message(time):
    now = datetime.now()
    deadline = datetime(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second,
    )
    if deadline >= now:
        prefix = "Осталось "
    else:
        prefix = "Просрочено на "
    weeks_part, days_part = '', ''
    time_left = deadline - now
    weeks, days = 0, 0
    if time_left.days >= 1:
        if time_left.days >= DAY_IN_WEEK:
            weeks = time_left.days // DAY_IN_WEEK
            weeks_part = f' {weeks} н.'
        days = time_left.days % DAY_IN_WEEK
        weeks_part = f' {days} д.'
    hours = time_left.seconds // (MIN_IN_H * SEC_IN_MIN)
    hours_part = f' {hours} ч.'
    minutes = (time_left.seconds % (MIN_IN_H * SEC_IN_MIN)) // SEC_IN_MIN
    minutes_part = f' {minutes} мин.'
    left_time_message = (f'{prefix}{weeks_part}{days_part}'
                         f'{hours_part}{minutes_part}')
    return left_time_message
