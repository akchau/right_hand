from datetime import datetime

MIN_IN_H = 60
SEC_IN_MIN = 60
DAY_IN_WEEK = 7
SEC_IN_HOUR = MIN_IN_H * SEC_IN_MIN


def get_format_datetime(time):
    time_if_format = datetime(
        time.year,
        time.month,
        time.day,
        time.hour,
        time.minute,
        time.second,
    )
    return time_if_format


def comparison_of_two_times(main, sub):
    return sub > main


def string_time_format(prefix, time, postfix):

    def get_string(number, unit):
        return f' {number} {unit}'

    time_left = time - datetime.now()

    seconds = time_left.seconds
    days = time_left.days

    # Добавляем префикс
    message = prefix

    # Это блок добавит к сообщению часы если они есть
    if seconds >= SEC_IN_MIN:

        # Это блок добавит к сообщению часы если они есть
        if seconds >= SEC_IN_HOUR:

            # Это блок добавит к сообщению дни если они есть
            if days >= 1:

                # Это блок добавит к сообщению недели если они есть
                if days >= DAY_IN_WEEK:

                    # Добавляем недели
                    message = message + get_string(
                        days // DAY_IN_WEEK, 'н'
                    )

                # Добавляем дни
                message = message + get_string(
                    days % DAY_IN_WEEK, 'д'
                )

            # Добавляем часы
            message = message + get_string(
                seconds // SEC_IN_HOUR, 'ч'
            )

        # Добавляем минуты
        message = message + get_string(
            (seconds % SEC_IN_HOUR) // SEC_IN_MIN, 'мин'
        )

        # Добавляем постфикс
        message = message + postfix

    # Если осталось меньше минуты
    else:
        message = "Сейчас"

    return message


# ___________________Методы для вызова_________________________
def get_time_left_message(time):
    """
    Метод который получает на вход дату дедлайна объекта.
    И возвращает сообщение об оставшемся/просроченном времени
    """
    deadline = get_format_datetime(time)
    if comparison_of_two_times(deadline, datetime.now()):
        prefix = "Просрочено на "
    else:
        prefix = "Осталось "
    postfix = ""
    return string_time_format(prefix, deadline, postfix)


def get_is_expired(time):
    deadline = get_format_datetime(time)
    return comparison_of_two_times(deadline, datetime.now())


def get_time_created_message(time):
    create_time = get_format_datetime(time)
    prefix = "Созд:"
    postfix = "назад"
    return string_time_format(prefix, create_time, postfix)


def get_time_updtaed_message(time):
    create_time = get_format_datetime(time)
    prefix = "Изм:"
    postfix = "назад"
    return string_time_format(prefix, create_time, postfix)
