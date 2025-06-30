from fastmcp import FastMCP
from src.encryption import caesar_encrypt, caesar_decrypt
from src.mailer import send_email

mcp = FastMCP(
    name="encryptme"
)

@mcp.tool(name="save_encrypted_note")
def save_note(text: str, shift: int, to: str, subject: str = "Your Encrypted Note") -> str:
    """Save the notes by first encrpting it and mailing to admin"""
    cipher = caesar_encrypt(text, shift)
    result = send_email(to, subject, cipher)
    return f"Note encrypted and sent. Message: {result}"

@mcp.tool(name="decrypt_note")
def decrypt_note(cipher: str, shift: int) -> str:
    """Just decrypt the message"""
    return caesar_decrypt(cipher, shift)

@mcp.tool(name="send_note")
def send_note(to: str, subject: str, body: str) -> str:
    """Just send notes"""
    return send_email(to, subject, body)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)