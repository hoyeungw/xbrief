def isnumeral(x):
    if isinstance(x, float):
        return True
    elif isinstance(x, int):
        return True
    elif isinstance(x, str):
        return x.isnumeric()
    else:
        return False
