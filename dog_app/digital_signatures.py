from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
import os

def sign_data(data):
    # Get key from environment
    pem_private = os.getenv('PEM_KEY')
    if pem_private is None:
        return "Server is not set up for signing data"
    return sign_data_with_key(data, pem_private)

def sign_data_with_key(data, pem_private):
    try:
        # Load the private key from PEM format
        private_key = serialization.load_pem_private_key(pem_private.encode(), password=None)

        # Create a signature
        signature = private_key.sign(
            data.encode(),
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return base64.b64encode(signature).decode('utf-8')
    except ValueError as e:
        print(f"Error loading private key: {e}")
        return None
    except Exception as e:
        print(f"Error signing data: {e}")
        return None
