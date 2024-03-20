#!/usr/bin/env python3

import numpy as np
import math, time, sys
from PIL import Image
from arnold import Arnold

def main(argv):
    image_name = "lena_color.tiff"  # Assuming you've changed the image to a colored version
    image_path = "images/" + image_name

    # Arnold Transform Parameters
    a = 6
    b = 40
    rounds = 33

    # Open the image
    img = Image.open(image_path)
    lena = np.array(img)  # This will now have a shape of (height, width, 3)

    print(" ~~~~~~  * PARAMETERS *  ~~~~~~ ")
    arnold = Arnold(a, b, rounds)
    print("\ta:\t", a)
    print("\tb:\t", b)
    print("\trounds:\t", rounds)

    print("\n ~~~~~~  *  RESULTS   *  ~~~~~~ ")
    
    scrambled_channels = []
    start_time = time.time()
    # Apply transformation to each channel
    for i in range(3):  # Iterate over each color channel
        channel = lena[:, :, i]
        scrambled_channel = arnold.applyTransformTo(channel)
        scrambled_channels.append(scrambled_channel)
    scrambled = np.stack(scrambled_channels, axis=-1)  # Reassemble the color channels
    exec_time = time.time() - start_time
    print("Transform execution time: %.6f sec" % exec_time)
    Image.fromarray(scrambled).save("scrambled.tif", format="TIFF")

    reconstructed_channels = []
    start_time = time.time()
    # Apply inverse transformation to each channel
    for i in range(3):
        channel = scrambled[:, :, i]
        reconstructed_channel = arnold.applyInverseTransformTo(channel)
        reconstructed_channels.append(reconstructed_channel)
    reconstructed = np.stack(reconstructed_channels, axis=-1)  # Reassemble the color channels
    exec_time = time.time() - start_time
    print("Inverse T. execution time: %.6f sec" % exec_time)
    Image.fromarray(reconstructed).save("reconstructed.tif", format="TIFF")

    # Counting different pixels is more complex with three channels,
    # and might need to be adjusted depending on your exact requirements.

if __name__ == "__main__":
    main(sys.argv[1:])
