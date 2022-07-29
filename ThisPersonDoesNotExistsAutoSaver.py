# Version 2.
import os
import uuid
import time

# How many images to download.
download_count = 2
# Adds to the name. Shows on console how many images have been downloaded.
img_counter = 0
# Delay between downloading images in seconds.
delay_in_seconds = 5

while img_counter < download_count:
    # Shell command that downloads the image. Uses img_counter and
    # UUID to prevent repeated names.
    # Example: 0_c15fa2cf-2aea-4e85-9ce1-4f394140537f.jpg
    os.system("curl -o " + str(img_counter) + "_" + str(uuid.uuid4()) +
              ".jpg https://thispersondoesnotexist.com/image")
    # Delay before downloading a new image.
    time.sleep(delay_in_seconds)
    # Counter raised.
    img_counter = img_counter + 1
