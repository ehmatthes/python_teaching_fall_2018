from PIL import Image

filename = 'willie_crab.jpg'

# Read in original image.
orig_img = Image.open(filename)
print("Original image:", orig_img.mode, orig_img.size)

# Load pixels.
#  This code loads all the pixels from the original image.
pixel_map = orig_img.load()

# This code creates a new image that matches the size of the original
#  image. It also sets all the pixels in the new image to white.
new_img = Image.new(orig_img.mode, orig_img.size, 'white')

# Get all the pixels in the new image.
#  We're free to change these pixels in any way we want.
#  First, we'll just copy the old pixels to the new image.
new_img_pixel_map = new_img.load()

# Modify each pixel in the new image.
for x in range(orig_img.size[0]):
    for y in range(orig_img.size[1]):
        
        # This gets the original r, g, and b values
        r = pixel_map[x,y][0]
        g = pixel_map[x,y][1]
        b = pixel_map[x,y][2]

        # This finds the average of the three rgb values, and uses that
        #  for each of the new rgb values.
        #  The // operator is normal division, but then only keeps the integer part of the quotient.
        avg_rgb = (r + g + b)//3
        max_rgb = max(r, g, b)
        new_r = max_rgb
        new_g = max_rgb
        new_b = max_rgb

        # This places each new pixel on the new image's pixel map.
        new_img_pixel_map[x, y] = (new_r, new_g, new_b)

# Show the image.
new_img.show()

# Save the image.
new_filename = f"modified_{filename}"
new_img.save(new_filename)
print(f"Saved {new_filename}.")