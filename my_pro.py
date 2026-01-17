import qrcode
import os

def generate_upi_qr(upi_id, name, amount, note):
    """
    Generates a UPI payment QR code URL and saves it as a PNG image.
    """
    # Standard UPI URI format for 2026 transactions
    # Note: The 'am' (amount) parameter should be a string
    upi_url = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&tn={note}&cu=INR"
    
    # Generate the QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(upi_url)
    qr.make(fit=True)
    qr.print_ascii()
    # Save as PNG
    img = qr.make_image(fill_color="black", back_color="white")
    file_path = "payment_qr.png"
    img.save(file_path)
    print(f"✅ QR Code generated successfully: {os.path.abspath(file_path)}")

if __name__ == "__main__":
    # --- PLACEHOLDERS ONLY ---
    # These IDs are fake and only for project demonstration. 
    # Replace with real IDs only on your local copy, never push them to GitHub.
    USER_UPI = "faijul.islam.01@axis" 
    USER_NAME = "Faijul Islsm"
    AMOUNT = "500.50" 
    MESSAGE = "Donation for GitHub Project"
    
    generate_upi_qr(USER_UPI, USER_NAME, AMOUNT, MESSAGE)

