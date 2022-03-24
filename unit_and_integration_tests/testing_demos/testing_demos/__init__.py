from django.core.exceptions import ValidationError


def validate_greater_than_zero(value):
    if value <= 0:
        raise ValidationError('Value must be greater than 0')


def get_only_positive_values(values):
    positive_values = []
    for value in values:
        try:
            validate_greater_than_zero(value)
            positive_values.append(value)
        except:
            pass

    return positive_values