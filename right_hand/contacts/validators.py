from django.core.exceptions import ValidationError

MIN_LEN_FIELDS = {
    'inn': 10,
    'kpp': 9,
}


def validate_mobile_phone_number(value):
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


def validate_inn(value):
    data = value.strip()
    numbers_all = [str(x) for x in range(10)]
    for sign in data:
        if sign not in numbers_all:
            raise ValidationError('Неверные символы. ИНН состоит из цифр.')
    len_number = len(data)
    if len_number < 10 or len_number > 12 or len_number == 11:
        raise ValidationError(
            'Неверная длинна ИНН. Для Юр.лица - 10 цифр, '
            f'для Физ.лица - 12 цифр. Введено - {len_number} цифр'
        )


def validate_kpp(value):
    data = value.strip()
    numbers_all = [str(x) for x in range(10)]
    for sign in data:
        if sign not in numbers_all:
            raise ValidationError(
                'Неверные символы. КПП состоит только из цифр.')
    len_number = len(data)
    if len_number < 9 or len_number > 9:
        raise ValidationError(
            'Неверная длинна КПП. КПП состоит'
            f'из 9 цифр. Введено - {len_number} цфифр'
        )


def validate_okpo(value):
    data = value.strip()
    numbers_all = [str(x) for x in range(10)]
    for sign in data:
        if sign not in numbers_all:
            raise ValidationError(
                'Неверные символы. ОКПО состоит только из цифр.')
    len_number = len(data)
    if len_number < 8 or len_number > 10 or len_number == 9:
        raise ValidationError(
            'Неверная длинна ОКПО. Для Юр.лица - 8 цифр, '
            f'для Физ.лица(ИП) - 10 цифр. Введено - {len_number} цифр'
        )
