#!/usr/bin/env python3

import numpy as np
import time  # Import time for execution time measurement
from PIL import Image
from arnold import Arnold
from fibQ import FibonacciQMatrix

def main(image_path):
    # Arnold Transform Parameters
    a = 6
    b = 40
    base_rounds = 251

    # Dynamic adjustment using Fibonacci Q-matrix
    fib_adjustment = FibonacciQMatrix.fib(5)  # Example: Using the 5th Fibonacci number to adjust parameters dynamically
    rounds = base_rounds + fib_adjustment

    print("~~~~~~ * PARAMETERS * ~~~~~~")
    print(f"\ta:\t{a}")
    print(f"\tb:\t{b}")
    print(f"\tInitial rounds:\t{base_rounds}")
    print(f"\tFibonacci adjustment:\t{fib_adjustment}")
    print(f"\tAdjusted rounds:\t{rounds}\n")

    # Initialize the Arnold transformation with adjusted parameters
    arnold = Arnold(a, b, rounds)
    
    # Open and process the image
    img = Image.open(image_path)
    img_array = np.array(img)  # Convert image to a NumPy array
    
    # Scrambling Process
    print("~~~~~~ * SCRAMBLING PROCESS * ~~~~~~")
    scrambled_channels = []
    start_time = time.time()  # Start timing
    for i in range(3):  # Process each channel with Arnold transform
        channel = img_array[:, :, i]
        scrambled_channel = arnold.applyTransformTo(channel)
        scrambled_channels.append(scrambled_channel)
    scrambled = np.stack(scrambled_channels, axis=-1)  # Reassemble the color channels
    exec_time = time.time() - start_time  # Calculate execution time
    print(f"Transform execution time: {exec_time:.6f} sec")
    Image.fromarray(scrambled).save("scrambled.tif", format="TIFF")

    # Unscrambling Process
    print("~~~~~~ * UNSCRAMBLING PROCESS * ~~~~~~")
    reconstructed_channels = []
    start_time = time.time()  # Start timing for inverse transformation
    for i in range(3):  # Process each channel with inverse Arnold transform
        channel = scrambled[:, :, i]
        reconstructed_channel = arnold.applyInverseTransformTo(channel)
        reconstructed_channels.append(reconstructed_channel)
    reconstructed = np.stack(reconstructed_channels, axis=-1)
    exec_time = time.time() - start_time  # Calculate execution time for inverse transformation
    print(f"Inverse T. execution time: {exec_time:.6f} sec")
    Image.fromarray(reconstructed).save("reconstructed.tif", format="TIFF")

if __name__ == "__main__":
    image_path = "images/lena_color.tiff"  # Example image path
    main(image_path)

   









# #with prints
# #!/usr/bin/env python3

# import numpy as np
# import time
# from PIL import Image
# from arnold import Arnold
# from fibQ import FibonacciQMatrix

# def main(image_path):
#     # Arnold Transform Parameters
#     a = 6
#     b = 40
#     base_rounds = 33

#     # Dynamic adjustment using Fibonacci Q-matrix
#     fib_adjustment = FibonacciQMatrix.fib(10)  # Using the 10th Fibonacci number to adjust parameters
#     rounds = base_rounds + fib_adjustment

#     # Printing the parameters used for the transformation
#     print("~~~~~~ * PARAMETERS * ~~~~~~")
#     print(f"\ta:\t{a}")
#     print(f"\tb:\t{b}")
#     print(f"\tInitial rounds:\t{base_rounds}")
#     print(f"\tFibonacci adjustment:\t{fib_adjustment}")
#     print(f"\tAdjusted rounds:\t{rounds}\n")
#     print("The parameters for Arnold's Cat Map have been dynamically adjusted using the 10th Fibonacci number, showcasing the integration of the Fibonacci Q-Matrix with Arnold's transformation technique.")

#     # Initialize the Arnold transformation with adjusted parameters
#     arnold = Arnold(a, b, rounds)

#     # Open and process the image
#     img = Image.open(image_path)
#     img_array = np.array(img)  # Convert image to a NumPy array
#     print("Image loaded and converted to a NumPy array.")

#     # Generate Fibonacci mask for encryption
#     height, width, _ = img_array.shape
#     fib_mask = FibonacciQMatrix.generate_fibonacci_mask(width, height)
#     print("Fibonacci mask generated for the image, employing the Q-Matrix method for encryption and decryption.")

#     # Apply Fibonacci Q-Matrix Encryption
#     print("~~~~~~ * FIBONACCI ENCRYPTION * ~~~~~~")
#     encrypted_image = np.empty_like(img_array)
#     for i in range(3):  # Apply mask to each channel
#         encrypted_image[:, :, i] = FibonacciQMatrix.encrypt_decrypt_image(img_array[:, :, i], fib_mask)
#     print("Image encrypted using the Fibonacci Q-Matrix. This step introduces the first layer of encryption, making the image data secure against straightforward attacks.")

#     # Scrambling Process with Arnold's Cat Map
#     print("~~~~~~ * SCRAMBLING PROCESS * ~~~~~~")
#     scrambled_channels = []
#     start_time = time.time()
#     for i in range(3):
#         channel = encrypted_image[:, :, i]
#         scrambled_channel = arnold.applyTransformTo(channel)
#         scrambled_channels.append(scrambled_channel)
#     scrambled = np.stack(scrambled_channels, axis=-1)
#     exec_time = time.time() - start_time
#     print(f"Arnold's Cat Map scrambling execution time: {exec_time:.6f} sec. The image has now been scrambled, further enhancing the encryption by rearranging pixel positions.")

#     # Save scrambled image for analysis
#     Image.fromarray(scrambled).save("scrambled.tif", format="TIFF")
#     print("Scrambled image saved as 'scrambled.tif'. This image represents the intermediate encrypted state, ideal for analysis and comparison.")

#     # Unscrambling Process with Arnold's Cat Map
#     print("~~~~~~ * UNSCRAMBLING PROCESS * ~~~~~~")
#     reconstructed_channels = []
#     start_time = time.time()
#     for i in range(3):
#         channel = scrambled[:, :, i]
#         reconstructed_channel = arnold.applyInverseTransformTo(channel)
#         reconstructed_channels.append(reconstructed_channel)
#     reconstructed_encrypted = np.stack(reconstructed_channels, axis=-1)
#     exec_time = time.time() - start_time
#     print(f"Inverse transformation execution time: {exec_time:.6f} sec. Arnold's Cat Map has been reversed, bringing the image back to its encrypted state prior to scrambling.")

#     # Apply Fibonacci Q-Matrix Decryption
#     print("~~~~~~ * FIBONACCI DECRYPTION * ~~~~~~")
#     reconstructed_image = np.empty_like(reconstructed_encrypted)
#     for i in range(3):
#         reconstructed_image[:, :, i] = FibonacciQMatrix.encrypt_decrypt_image(reconstructed_encrypted[:, :, i], fib_mask)
#     print("Fibonacci Q-Matrix decryption applied. The image has been successfully decrypted, showcasing the reversibility and effectiveness of the combined encryption method.")

#     # Save reconstructed image for analysis
   
























































































#!/usr/bin/env python3

# import numpy as np
# import time  # Import time for execution time measurement
# from PIL import Image
# from arnold import Arnold
# from fibQ import FibonacciQMatrix

# def main(image_path):
#     # Arnold Transform Parameters
#     a = 6
#     b = 40
#     base_rounds = 33

#     # Dynamic adjustment using Fibonacci Q-matrix
#     fib_adjustment = FibonacciQMatrix.fib(10)  # Example: Using the 5th Fibonacci number to adjust parameters dynamically
#     rounds = base_rounds + fib_adjustment

#     print("~~~~~~ * PARAMETERS * ~~~~~~")
#     print(f"\ta:\t{a}")
#     print(f"\tb:\t{b}")
#     print(f"\tInitial rounds:\t{base_rounds}")
#     print(f"\tFibonacci adjustment:\t{fib_adjustment}")
#     print(f"\tAdjusted rounds:\t{rounds}\n")

#     # Initialize the Arnold transformation with adjusted parameters
#     arnold = Arnold(a, b, rounds)
    
#     # Open and process the image
#     img = Image.open(image_path)
#     img_array = np.array(img)  # Convert image to a NumPy array
    
#     # Scrambling Process
#     print("~~~~~~ * SCRAMBLING PROCESS * ~~~~~~")
#     scrambled_channels = []
#     start_time = time.time()  # Start timing
#     for i in range(3):  # Process each channel with Arnold transform
#         channel = img_array[:, :, i]
#         scrambled_channel = arnold.applyTransformTo(channel)
#         scrambled_channels.append(scrambled_channel)
#     scrambled = np.stack(scrambled_channels, axis=-1)  # Reassemble the color channels
#     exec_time = time.time() - start_time  # Calculate execution time
#     print(f"Transform execution time: {exec_time:.6f} sec")
#     Image.fromarray(scrambled).save("scrambled.tif", format="TIFF")

#     # Unscrambling Process
#     print("~~~~~~ * UNSCRAMBLING PROCESS * ~~~~~~")
#     reconstructed_channels = []
#     start_time = time.time()  # Start timing for inverse transformation
#     for i in range(3):  # Process each channel with inverse Arnold transform
#         channel = scrambled[:, :, i]
#         reconstructed_channel = arnold.applyInverseTransformTo(channel)
#         reconstructed_channels.append(reconstructed_channel)
#     reconstructed = np.stack(reconstructed_channels, axis=-1)
#     exec_time = time.time() - start_time  # Calculate execution time for inverse transformation
#     print(f"Inverse T. execution time: {exec_time:.6f} sec")
#     Image.fromarray(reconstructed).save("reconstructed.tif", format="TIFF")

# if __name__ == "__main__":
#     image_path = "images/lena_color.tiff"  # Example image path
#     main(image_path)



























# #!/usr/bin/env python3

# import numpy as np
# from PIL import Image

# # Ensure these custom modules are correctly implemented and present
# from arnold import Arnold
# from fibQ import FibonacciQMatrix

# def main(image_path):
#     try:
#         # Arnold Transform Parameters
#         a = 6
#         b = 40
#         base_rounds = 33

#         # Dynamic adjustment using Fibonacci Q-matrix
#         fib_adjustment = FibonacciQMatrix.fib(10)  # Adjust parameters dynamically
#         rounds = base_rounds + fib_adjustment

#         print("~~~~~~ * PARAMETERS * ~~~~~~")
#         print(f"\ta:\t{a}")
#         print(f"\tb:\t{b}")
#         print(f"\tInitial rounds:\t{base_rounds}")
#         print(f"\tFibonacci adjustment:\t{fib_adjustment}")
#         print(f"\tAdjusted rounds:\t{rounds}\n")

#         # Initialize Arnold transformation
#         arnold = Arnold(a, b, rounds)

#         # Process the image
#         img = Image.open(image_path)
#         img_array = np.array(img)

#         # Encryption and Scrambling
#         height, width, _ = img_array.shape
#         fib_mask = FibonacciQMatrix.generate_fibonacci_mask(width, height)

#         print("~~~~~~ * ENCRYPTION AND SCRAMBLING * ~~~~~~")
#         # Encryption and scrambling logic follows...

#         # Placeholder for the rest of the encryption and scrambling process
#         # ...

#     except Exception as e:
#         print(f"Error: {e}")

# if __name__ == "__main__":
#     image_path = "images/lena_color.tiff"
#     main(image_path)
