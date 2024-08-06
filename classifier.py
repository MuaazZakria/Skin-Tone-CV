import stone
import math
import cv2
image_path = 'Data//test.PNG'

result = stone.process(image_path, image_type="color", return_report_image=True)

# Define example RGB values for each skin tone category
# skin_tone_examples = {
#     "pale": [(255, 224, 189)],
#     "light": [(255, 205, 178)],
#     "medium": [(224, 172, 105)],
#     "tan": [(204, 142, 105)],
#     "deep": [(139, 108, 66)],
#     "dark": [(80, 52, 36)]
# }
skin_tone_examples = {
    "light": [(247, 218, 200), (234, 238, 183), (237, 221, 205), (232, 199, 179), (229, 204, 199), (235, 218, 207), (232, 192, 183)],
    "pale": [(241, 206, 199), (246, 201, 177), (239, 193, 166), (229, 195, 161), (235, 184, 150)],
    "medium": [(238, 185, 138), (229, 171, 117), (226, 158, 105), (220, 182, 141), (213, 170, 134), (214, 144, 86)],
    "Tanned": [(199, 160, 124), (171, 138, 119), (150, 121, 101), (167, 133, 94), (157, 110, 63),(142, 122, 86)],
    "dark/deep": [(136, 114, 96), (134, 90, 51), (118, 75, 41), (147, 98, 67), (134, 85, 52), (122, 71, 40)],
    "black": [(99, 53, 23), (81, 53, 33), (81, 63, 55), (70, 51, 37), (80, 36, 10), (68, 20, 6)]
}


def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))


def euclidean_distance(rgb1, rgb2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(rgb1, rgb2)))


def get_skin_tone_category(rgb_value):
    closest_category = "unknown"
    smallest_distance = float('inf')
    for category, examples in skin_tone_examples.items():
        for example in examples:
            distance = euclidean_distance(rgb_value, example)
            print(distance, category)
            if distance < smallest_distance:
                smallest_distance = distance
                closest_category = category
    return closest_category


for face in result["faces"]:
    rgb_value = hex_to_rgb(face["skin_tone"])
    print(face["skin_tone"],'hex value')
    print(rgb_value, 'gggg')
    category = get_skin_tone_category(rgb_value)
    print(f"Face ID {face['face_id']} has skin tone category: {category}")

report_images = result.pop("report_images")  # obtain and remove the report image from the `result`
print(result)
face_id = 1
cv2.imshow('image', report_images[face_id])

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()

# cv2_imshow(report_images[face_id]) # Use `stone.show` instead in Python scripts
