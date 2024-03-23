class FibonacciQMatrix:
    @staticmethod
    def matrix_multiply(A, B):
        """Multiplies two matrices A and B."""
        return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    @staticmethod
    def matrix_power(A, n):
        """Computes the nth power of matrix A using exponentiation by squaring."""
        if n == 1:
            return A
        if n % 2 == 0:
            return FibonacciQMatrix.matrix_power(FibonacciQMatrix.matrix_multiply(A, A), n // 2)
        else:
            return FibonacciQMatrix.matrix_multiply(A, FibonacciQMatrix.matrix_power(FibonacciQMatrix.matrix_multiply(A, A), (n - 1) // 2))

    @staticmethod
    def fib(n):
        """Computes the nth Fibonacci number using the Q-matrix method."""
        if n == 0:
            return 0
        Q = [[1, 1], [1, 0]]
        Qn = FibonacciQMatrix.matrix_power(Q, n)
        return Qn[0][1]  # The nth Fibonacci number is the off-diagonal element of Q^n

    @staticmethod
    def generate_fibonacci_mask(width, height):
        """Generates a Fibonacci mask for an image of specified dimensions."""
        mask = []
        for i in range(height):
            row = []
            for j in range(width):
                # Compute the Fibonacci number for the current position in the sequence
                fib_number = FibonacciQMatrix.fib(i * width + j + 1) % 256  # Use mod 256 to keep within byte range
                row.append(fib_number)
            mask.append(row)
        return mask

    @staticmethod
    def encrypt_decrypt_image(image_data, mask):
        """Encrypts or decrypts image data using the provided Fibonacci mask."""
        encrypted_decrypted_data = []
        for i, row in enumerate(image_data):
            encrypted_decrypted_row = [pixel ^ mask_pixel for pixel, mask_pixel in zip(row, mask[i])]
            encrypted_decrypted_data.append(encrypted_decrypted_row)
        return encrypted_decrypted_data






# Application to Image Encryption
# The generate_fibonacci_mask method generates a mask of Fibonacci numbers that can be applied to the pixels of an image. The mask is designed to fit the dimensions of the image, with each pixel's value being modified based on the corresponding value in the Fibonacci mask. This operation can be as simple as a bitwise XOR between the pixel values and the mask, or more complex manipulations can be designed as needed.

# The encryption process would involve applying this mask to the image data, followed by the Arnold cat map scrambling. Decryption would reverse this process, first applying the inverse Arnold cat map and then reversing the Fibonacci mask application.

# This method introduces a layer of encryption that directly manipulates pixel values using a sequence derived from the Fibonacci Q-matrix, offering a novel approach to image encryption. However, the effectiveness and security of this method would need thorough analysis and testing in cryptographic and image processing research.










































# fibQ.py
# class FibonacciQMatrix:
#     @staticmethod
#     def matrix_multiply(A, B):
#         """Multiplies two matrices A and B."""
#         return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

#     @staticmethod
#     def matrix_power(A, n):
#         """Computes the nth power of matrix A using exponentiation by squaring."""
#         if n == 1:
#             return A
#         if n % 2 == 0:
#             return FibonacciQMatrix.matrix_power(FibonacciQMatrix.matrix_multiply(A, A), n // 2)
#         else:
#             return FibonacciQMatrix.matrix_multiply(A, FibonacciQMatrix.matrix_power(FibonacciQMatrix.matrix_multiply(A, A), (n - 1) // 2))

#     @staticmethod
#     def fib(n):
#         """Computes the nth Fibonacci number using the Q-matrix method."""
#         if n == 0:
#             return 0
#         Q = [[1, 1], [1, 0]]
#         Qn = FibonacciQMatrix.matrix_power(Q, n)
#         return Qn[0][1]  # The nth Fibonacci number is the off-diagonal element of Q^n
