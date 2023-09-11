import locale

def intToIDR(numberInt, prefix=False, decimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    idr = locale.format("%.*f", (decimal, numberInt), True)
    if prefix:
        return format(idr)
    return idr
