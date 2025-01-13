from cryptography.fernet import Fernet
import json

# Funksioni për të krijuar një çelës të ri dhe për të ruajtur atë në një skedar
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Çelësi u krijua dhe u ruajt në 'secret.key'.")

# Funksioni për të lexuar çelësin nga skedari
def load_key():
    return open("secret.key", "rb").read()

# Funksioni për të enkriptuar të dhënat
def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

# Funksioni për të dekriptuar të dhënat
def decrypt_data(encrypted_data):
    key = load_key()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

# Funksioni për enkriptimin e të dhënave nga skedari JSON
def encrypt_quotes():
    # Lexoni të dhënat nga skedari quotes.json
    with open('quotes.json', 'r', encoding='utf-8') as f:
        data = f.read()

    # Enkriptuam të dhënat
    encrypted_data = encrypt_data(data)

    # Ruaj të dhënat e enkriptuara në një skedar
    with open('encrypted_quotes.json', 'wb') as f:
        f.write(encrypted_data)

    print("Të dhënat u enkriptuan dhe u ruajtën në 'encrypted_quotes.json'.")

# Funksioni për dekriptimin e të dhënave
def decrypt_and_read():
    # Lexoni të dhënat e enkriptuara nga skedari
    with open('encrypted_quotes.json', 'rb') as f:
        encrypted_data = f.read()

    # Dekriptojmë të dhënat dhe i shfaqim
    decrypted_data = decrypt_data(encrypted_data)
    print("Të dhënat e dekriptuara:")
    print(decrypted_data)

if __name__ == "__main__":
    # Krijoni çelësin nëse nuk është krijuar ende
    generate_key()

    # Enkripto të dhënat nga quotes.json dhe i ruaj
    encrypt_quotes()

    # Dekripto dhe shiko të dhënat
    decrypt_and_read()
