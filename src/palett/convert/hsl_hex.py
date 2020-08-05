from palett.convert import hsl_rgb, rgb_hex


def hsl_hex(hsl):
    return rgb_hex(hsl_rgb(hsl))
