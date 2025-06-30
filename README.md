
# 🔐 SecureNote Agent

A lightweight Claude-style MCP Agent built in Python using `FastMCP` that allows you to:
- Encrypt messages using Caesar Cipher
- Decrypt messages locally
- Send encrypted or plaintext notes via email (SMTP)

This can be used as a personal secure note-mailing backend or as an MCP plugin agent for Claude Desktop or OpenRouter.

---

## 🚀 Features

- 🔐 Encrypt any text using Caesar cipher (`encrypt_note`)
- 🔓 Decrypt an encrypted message (`decrypt_note`)
- 📧 Send secure or regular emails via SMTP (`send_note`)
- 🧠 MCP Agent format supported by Claude Desktop

---

## 🧱 Tech Stack

- Python
- `FastMCP` / `mcp.server.fastmcp`
- FastAPI (automatically used by MCP)
- SMTP (Gmail-compatible)
- Claude/LLM-compatible via local plugin tooling

---

## 📁 Project Structure

```
securenote-agent/
├── main.py            # MCP agent entrypoint
├── encryption.py      # Caesar cipher functions
├── mailer.py          # SMTP logic
├── requirements.txt   # Dependencies
├── mcp.json           # Plugin metadata (optional)
└── claude.agent.json  # Claude Desktop config (optional)
```

---

## 🔧 Setup Instructions

### 1. Clone + Install

```bash
git clone https://github.com/yourusername/securenote-agent.git
cd securenote-agent
pip install -r requirements.txt
```

### 2. Configure Email

Update `mailer.py` with your Gmail or SMTP credentials.

```python
from_address = "your@gmail.com"
password = "your_app_password"
```

> 📌 Use an **App Password** if using Gmail with 2FA.

---

## 🚀 Run MCP Agent (HTTP mode)

```bash
python main.py
```

Ensure your `main.py` ends with:

```python
if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)
```

---

## 🌐 Try in Browser

Go to:
```
http://localhost:8000/docs
```

You can now test:
- `/encrypt_note`
- `/decrypt_note`
- `/send_note`

---

## 🤖 Claude Agent (Optional)

If using Claude Desktop or Claude CLI:

### `claude.agent.json`
```json
{
  "schema_version": "v1",
  "name": "SecureNote Agent",
  "description": "Encrypt, decrypt and email secure notes via Claude MCP tool",
  "entry_point": "main.py",
  "runtime": "mcp",
  "api": {
    "type": "mcp",
    "url": "http://localhost:8000/openapi.json"
  }
}
```

---

## 📌 Example Prompts for Claude

> "Encrypt the message `My ATM PIN is 4321` with shift 3 and email it to utsav@gmail.com"

> "Decrypt the message `Pb dww dfwlrq` with Caesar cipher and shift 3"

---

## 🧪 Testing API (Optional `test.http`)

```http
### Encrypt
POST http://localhost:8000/encrypt_note
Content-Type: application/json

{
  "text": "Hello World",
  "shift": 3
}

### Send Email
POST http://localhost:8000/send_note
Content-Type: application/json

{
  "to": "receiver@example.com",
  "subject": "Encrypted Note",
  "body": "Khoor Zruog"
}
```

---

## 🪪 License

MIT License

---

## ✍️ Author

Built with ❤️ by [Utsav Moradiya](https://utsavmoradiya.in)
