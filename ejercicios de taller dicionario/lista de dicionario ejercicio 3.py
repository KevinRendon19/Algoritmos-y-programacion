usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

intentos = 3

while intentos > 0:
    usuario = input("Introduce el nombre de usuario: ")
    contraseña = input("Introduce la contraseña: ")

    if usuario in usuarios and usuarios[usuario]['password'] == contraseña:
        nombre = usuarios[usuario]['nombre']
        apellido = usuarios[usuario]['apellido']
        print(f"Bienvenido, {nombre} {apellido}.")
        break
    else:
        intentos -= 1
        print(f"Usuario o contraseña incorrectos. Te quedan {intentos} intento(s).")

if intentos == 0:
    print("Has superado el número máximo de intentos. Acceso denegado.")