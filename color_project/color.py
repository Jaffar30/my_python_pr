import colorgram

def get_colors(image_colors):
    colors = []
    for color in image_colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        colors.append((r, g, b))
    return colors