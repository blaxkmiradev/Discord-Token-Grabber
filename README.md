<div align="center">
  <h1>🔥 Discord Token Grabber</h1>
  <p><strong>A clean & powerful Discord token stealer for educational purposes</strong></p>

  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Windows-Only-0078D4?style=for-the-badge&logo=windows" alt="Windows">
  <img src="https://img.shields.io/badge/Status-Working-green?style=for-the-badge" alt="Status">

  <br><br>
  <img src="https://i.imgur.com/8Z3Zf9K.png" width="600" alt="Banner">
</div>

---

## ✨ Features

- **Stealth Mode** – Hides console window automatically
- **Advanced Decryption** – Uses DPAPI + AES-GCM (same as Discord)
- **Smart Scanning** – Scans `.log` and `.ldb` files
- **Deduplication** – Removes duplicate tokens
- **Fast & Clean** – Lightweight and efficient
- **Webhook Delivery** – Sends tokens instantly to Discord

---

## 🛠️ How It Works

```text
1. Extracts encryption key from Local State
2. Scans Discord LevelDB folder
3. Decrypts tokens using master key
4. Validates & sends to your webhook
