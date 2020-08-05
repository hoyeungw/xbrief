from palett.convert import rgb_int

'''
@param {[number,number,number]} rgb
@returns {string}
'''


def rgb_hex(rgb):  # TODO: should convert to upper case
    return f'#{rgb_int(rgb):06x}'

    # return '#' + rgbToInt(rgb).toString(16).toUpperCase().padStart(6, '0')


def test():
    rgb_candidates = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'magenta': (255, 0, 255),
        'cyan': (0, 255, 255),
        'yellow': (255, 255, 0),
        'grey': (128, 128, 128)
    }
    for key, rgb in rgb_candidates.items():
        print(key, rgb, '->', rgb_hex(rgb))


test()
