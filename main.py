import colorgram

# my solution:

colors_from_image = colorgram.extract('image.jpg', 10)

color_list = []


def seperate_each_color(color_list, new_list):
    x = 0
    for _ in range(len(color_list)):
        color = color_list[x]
        r = color.rgb[0]
        g = color.rgb[1]
        b = color.rgb[2]
        color = (r, g, b)
        x += 1
        new_list.append(color)


seperate_each_color(colors_from_image, color_list)

print(color_list)


# teacher's solution:

