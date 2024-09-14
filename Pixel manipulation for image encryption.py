from PIL import Image
import numpy as np

def encrypt_image(input_image_path, output_image_path, key):
    """Encrypt the image by manipulating pixel values."""

    image = Image.open(input_image_path)
    pixels = np.array(image)

    # Encrypt the pixels using a simple mathematical operation (XOR with key)
    encrypted_pixels = pixels ^ key

    # Save the encrypted image
    encrypted_image = Image.fromarray(encrypted_pixels)
    encrypted_image.save(output_image_path)

def decrypt_image(input_image_path, output_image_path, key):
    """Decrypt the image by reversing the encryption process."""
    # Open the encrypted image
    encrypted_image = Image.open(input_image_path)
    pixels = np.array(encrypted_image)

    # Decrypt the pixels using the same operation (XOR with key)
    decrypted_pixels = pixels ^ key

    # Save the decrypted image
    decrypted_image = Image.fromarray(decrypted_pixels)
    decrypted_image.save(output_image_path)

def main():
    input_image_path = "nature.png"  # Change this to your input image path
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.png"

    key = 123  # Simple key for XOR operation (must be between 0-255)

    encrypt_image(input_image_path, encrypted_image_path, key)
    print(f"Encrypted image saved as {encrypted_image_path}")

    decrypt_image(encrypted_image_path, decrypted_image_path, key)
    print(f"Decrypted image saved as {decrypted_image_path}")

if __name__ == "__main__":
    main()
