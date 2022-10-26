from django.core.exceptions import ValidationError


def validate_phone_number(value):
    data = value.strip()
    elements = [
        '+',
        '-',
        ' ',
        ')',
        '(',
    ]
    numbers_all = [str(x) for x in range(10)]
    for element in elements:
        data = data.replace(element, '')
    for sign in data:
        if sign not in numbers_all:
            raise ValidationError('Неверные символы')
    len_number = len(data)
    if len_number < 10 or len_number > 11:
        raise ValidationError('Неверная длинна номера')
