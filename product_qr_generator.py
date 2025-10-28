# product_qr_generator.py

"""
📦 Product QR Code Generator

This script generates a QR code containing product information,
including expiration date calculations and ingredient details.

Dependencies:
- qrcode
- Pillow (automatically installed with qrcode)
"""

import qrcode
from datetime import datetime


def calculate_days_to_expire(expiration_date: str) -> int:
    """
    Calculate the number of days from today until the expiration date.

    Args:
        expiration_date (str): Expiration date in 'YYYY-MM-DD' format.

    Returns:
        int: Number of days until expiration.
    """
    today = datetime.today()
    exp_date = datetime.strptime(expiration_date, '%Y-%m-%d')
    return (exp_date - today).days


def generate_product_info(product_data: dict) -> str:
    """
    Convert product data dictionary to a formatted string.

    Args:
        product_data (dict): Dictionary containing product details.

    Returns:
        str: Formatted string of product info.
    """
    return "\n".join(f"{key}: {value}" for key, value in product_data.items())


def generate_qr_code(content: str, filename: str = "product_qr_code.png"):
    """
    Generate and save a QR code from the given content.

    Args:
        content (str): Text content to encode in the QR code.
        filename (str): Output filename for the QR image.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(content)
    qr.make(fit=True)

    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"✅ QR code generated and saved as '{filename}'")


if __name__ == "__main__":
    # --- Sample Product Data ---
    product_name = "Sample Product"
    ingredients = "Water, Sugar, Preservatives"
    manufacture_date = "2024-01-01"
    expiration_date = "2025-01-01"
    harmful_chemicals = "None"

    # Compute days until expiration
    days_to_expire = calculate_days_to_expire(expiration_date)

    # Prepare dictionary of product information
    product_info = {
        "Product Name": product_name,
        "Ingredients": ingredients,
        "Manufacture Date": manufacture_date,
        "Expiration Date": expiration_date,
        "Days to Expire": days_to_expire,
        "Harmful Chemicals": harmful_chemicals
    }

    # Generate and save QR code
    qr_content = generate_product_info(product_info)
    generate_qr_code(qr_content)
