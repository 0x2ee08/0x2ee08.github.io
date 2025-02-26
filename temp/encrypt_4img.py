import base64
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def encrypt_image(input_path, output_path, password):
    # Read the image file as binary
    with open(input_path, 'rb') as f:
        image_data = f.read()
    
    # Convert image to base64
    base64_data = base64.b64encode(image_data).decode('utf-8')
    
    # Create encryption key from password (ensure it's 16 bytes)
    key = password.ljust(16)[:16].encode('utf-8')
    
    # Create AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Pad the data to be a multiple of 16 bytes (AES block size)
    padded_data = pad(base64_data.encode('utf-8'), AES.block_size)
    
    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)
    
    # Convert to base64 for storage
    encrypted_base64 = base64.b64encode(encrypted_data).decode('utf-8')
    
    # Write the encrypted data to the output file
    with open(output_path, 'w') as f:
        f.write(encrypted_base64)
    
    print(f"Encrypted {input_path} -> {output_path}")

def encrypt_multiple_images(image_paths, output_dir, password):
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Process each image
    for i, image_path in enumerate(image_paths):
        # Get the filename without extension
        base_name = os.path.basename(image_path).split('.')[0]
        output_path = os.path.join(output_dir, f"{base_name}_encrypted.txt")
        
        encrypt_image(image_path, output_path, password)

# Example usage
if __name__ == "__main__":
    # List of only the 4 images to encrypt
    images = [
        "./secondary/THT.jpg",
        "./secondary/1.png",
        "./secondary/3.png",
        "./secondary/4.png"
    ]
    
    # Password for encryption
    password = "???"  # Replace with your desired password
    
    # Output directory for encrypted files
    output_dir = "./encrypted_images"
    
    encrypt_multiple_images(images, output_dir, password)