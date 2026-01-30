import json
import os

def es_mayor_de_edad(edad: int) -> bool:
    """Comprueba si el usuario tiene la edad legal."""
    return edad >= 18

def guardar_usuario(usuario: dict, filename: str = "usuarios.json"):
    """Guarda un usuario en el archivo JSON."""
    lista_usuarios = []
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            try:
                lista_usuarios = json.load(f)
            except json.JSONDecodeError:
                lista_usuarios = []

    lista_usuarios.append(usuario)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(lista_usuarios, f, indent=4, ensure_ascii=False)

def listar_usuarios(filename: str = "usuarios.json"):
    """Muestra los usuarios guardados en formato de tabla."""
    if not os.path.exists(filename):
        print("\n📭 La base de datos está vacía.")
        return

    with open(filename, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    if not usuarios:
        print("\n📭 No hay usuarios registrados.")
        return

    print("\n" + "="*50)
    print(f"{'ID':<4} | {'NOMBRE':<20} | {'EDAD':<5} | {'ESTADO'}")
    print("-" * 50)
    for i, user in enumerate(usuarios, start=1):
        estado = "✅ Adulto" if user["es_adulto"] else "🚫 Menor"
        print(f"{i:<4} | {user['nombre']:<20} | {user['edad']:<5} | {estado}")
    print("="*50 + "\n")

def menu_principal():
    """Muestra el menú y gestiona la navegación del usuario."""
    while True:
        print("--- SISTEMA DE GESTIÓN PRO ---")
        print("1. Registrar nuevo usuario")
        print("2. Listar todos los usuarios")
        print("3. Salir")
        
        opcion = input("\nSelecciona una opción (1-3): ").strip()

        match opcion:
            case "1":
                nombre = input("Nombre: ").strip()
                try:
                    edad = int(input("Edad: "))
                    usuario = {
                        "nombre": nombre,
                        "edad": edad,
                        "es_adulto": es_mayor_de_edad(edad)
                    }
                    guardar_usuario(usuario)
                    print(f"\n✅ {nombre} registrado correctamente.\n")
                except ValueError:
                    print("\n❌ Error: La edad debe ser un número.\n")
            
            case "2":
                listar_usuarios()
            
            case "3":
                print("\n👋 Saliendo del sistema. ¡Hasta pronto!")
                break
            
            case _:
                print("\n⚠️ Opción no válida, intenta de nuevo.\n")

if __name__ == "__main__":
    menu_principal()