from palett.convert import hex_rgb, rgb_hsl


def hex_hsl(hex_color):
    return rgb_hsl(hex_rgb(hex_color))
