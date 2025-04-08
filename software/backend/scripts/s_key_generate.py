# scripts/s_key_generate.py
import secrets

def generate_secret_key(length=128):
    return secrets.token_hex(length)

if __name__ == "__main__":
    key = generate_secret_key(64)  # 64 bytes = 128 hex characters
    print("\n🔑 Generated SECRET_KEY:\n")
    print(key)