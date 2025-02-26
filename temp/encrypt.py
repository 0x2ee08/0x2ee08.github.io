import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

# Configuration
image_path = "./gotIntoHS/IMG_9039.JPG"  # Path to your image
password = "???"  # Your chosen password (will be padded/truncated to 16 bytes)
output_file = "encrypted_image.txt"  # Where to save the encrypted string

# Step 1: Read image and convert to Base64
with open(image_path, "rb") as image_file:
    base64_string = base64.b64encode(image_file.read()).decode("utf-8")

# Step 2: Prepare the AES key (must be 16, 24, or 32 bytes)
key = password.encode("utf-8")
if len(key) < 16:
    key = key.ljust(16, b" ")  # Pad with spaces if too short
elif len(key) > 16:
    key = key[:16]  # Truncate if too long
# Now key is exactly 16 bytes for AES-128

# Step 3: Encrypt the Base64 string with AES
cipher = AES.new(key, AES.MODE_ECB)  # Using ECB mode for simplicity
padded_data = pad(base64_string.encode("utf-8"), AES.block_size)
encrypted = cipher.encrypt(padded_data)
encrypted_base64 = base64.b64encode(encrypted).decode("utf-8")

# Step 4: Save the encrypted string to a file
with open(output_file, "w") as f:
    f.write(encrypted_base64)

print(f"Encrypted Base64 string saved to {output_file}")
print(f"Use this password in your website: {password}")