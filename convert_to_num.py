def cnumf(value):
    value = value.strip()
    multiplier = 1

    if value.endswith('K'):
        multiplier = 1000
        value = value[:-1]
    elif value.endswith('M'):
        multiplier = 1000000
        value = value[:-1]
    elif value.endswith('B'):
        multiplier = 1000000000
        value = value[:-1]

    try:
        return int(value) * multiplier
    except ValueError:
        return 0