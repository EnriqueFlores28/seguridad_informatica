import hashlib
import webbrowser

def generar_hashes(texto):
    return {
        "MD5": hashlib.md5(texto.encode()).hexdigest(),
        "SHA-1": hashlib.sha1(texto.encode()).hexdigest(),
        "SHA-256": hashlib.sha256(texto.encode()).hexdigest(),
        "SHA-512": hashlib.sha512(texto.encode()).hexdigest()
    }

# Hashes almacenados (ejemplo: hash de "seguridad")
hashes_guardados = {
    "MD5": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd50a42fcab923eaed4",  # Hash de "password"
    "SHA-1": "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8",  # Hash de "password"
    "SHA-256": "b19d4271e8fffa924c8c693b39cb6a96864b8c6b705e88378a20ac7437c0e29d",
    "SHA-512": "4bb122efccd56691ddebd24ccd27c1fe43aa1eb875472e9ec668cb538ceddd5f46951730d0a44511728f248162df854e674ce5db5ff1ee745dbf45fd15b3d418" # Hash de "seguridad"
}

# Pedir entrada al usuario
palabra = input("Ingresa una palabra: ")
hashes_ingresados = generar_hashes(palabra)

# Comparar hashes
coincidencia = False
for algoritmo, hash_guardado in hashes_guardados.items():
    if hashes_ingresados[algoritmo] == hash_guardado:
        print(f"✅ La palabra ingresada coincide con el hash almacenado ({algoritmo}).")
        coincidencia = True
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        break

if not coincidencia:
    print("❌ La palabra ingresada no coincide con ningún hash almacenado.")