import colorgram

# my solution:

# colors_from_image = colorgram.extract('image.jpg', 30)
#
# color_list = []
#
#
# def separate_each_color(empty_colors_list, new_list):
#     x = 0
#     for _ in range(len(empty_colors_list)):
#         color = empty_colors_list[x]
#         r = color.rgb[0]
#         g = color.rgb[1]
#         b = color.rgb[2]
#         color = (r, g, b)
#         x += 1
#         new_list.append(color)
#
#
# separate_each_color(colors_from_image, color_list)
#
# print(color_list)
#

# teacher's solution:

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)


hirst_colors = [
    (232, 233, 236), (236, 230, 233), (225, 234, 229), (175, 48, 79), (43, 97, 146), (204, 162, 94), (223, 210, 103),
    (137, 90, 65), (110, 176, 206), (176, 164, 39), (211, 132, 173), (225, 74, 51), (199, 76, 119), (90, 105, 190),
    (27, 145, 91), (124, 218, 208), (95, 157, 64), (119, 43, 71), (227, 170, 187), (131, 187, 161), (49, 186, 201),
    (172, 186, 220), (233, 173, 164), (153, 208, 217), (98, 52, 44), (35, 64, 111), (43, 77, 80), (51, 59, 66),
    (73, 51, 44)
]
