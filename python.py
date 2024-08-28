import qrcode

def generate_qr_code(url, filename):
    """
    Generate a QR code from a URL and save it to a file.

    Args:
        url (str): The URL to encode in the QR code.
        filename (str): The filename to save the QR code as.
    """
    img = qrcode.make(url)
    img.save(filename)

# Example usage:
url = "youtube.com/channel/UCFgSE2vhM_j67mXERUB1slw"
filename = "your_qr_code.png"
generate_qr_code(url, filename)