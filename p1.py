import json
import os

# --- LÓGICA DE NEGOCIO ---

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def cargar_datos(filename: str = "usuarios.json") -> list:
    """Lee el archivo y retorna la lista de usuarios."""
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_datos(usuarios: list, filename: str = "usuarios.json"):
    """Guarda la lista completa en el JSON."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# --- NUEVAS FUNCIONES CRUD ---

def buscar_usuario():
    """Busca usuarios por coincidencia de nombre."""
    query = input("🔍 Introduce el nombre a buscar: ").strip().lower()
    usuarios = cargar_datos()
    
    # List comprehension: Una forma muy 'Pythonic' y pro de filtrar
    resultados = [u for u in usuarios if query in u["nombre"].lower()]
    
    if not resultados:
        print(f"\n❌ No se encontraron resultados para: '{query}'")
    else:
        print(f"\n✅ Se encontraron {len(resultados)} coincidencias:")
        for u in resultados:
            print(f"- {u['nombre']} ({u['edad']} años)")

def borrar_usuario():
    """Elimina un usuario por su nombre exacto."""
    nombre_a_borrar = input("🗑️ Nombre exacto del usuario a eliminar: ").strip()
    usuarios = cargar_datos()
    
    # Creamos una nueva lista EXCLUYENDO al usuario (así se borra en Python)
    nueva_lista = [u for u in usuarios if u["nombre"] != nombre_a_borrar]
    
    if len(nueva_lista) == len(usuarios):
        print(f"\n⚠️ No se encontró a '{nombre_a_borrar}'. Nada que borrar.")
    else:
        guardar_datos(nueva_lista)
        print(f"\n✨ Usuario '{nombre_a_borrar}' eliminado correctamente.")

# --- INTERFAZ DE USUARIO ---

def menu_principal():
    while True:
        print("\n" + "═"*30)
        print(" 🚀 SISTEMA DE GESTIÓN CRUD")
        print("═"*30)
        print("1. Registrar usuario")
        print("2. Listar todos")
        print("3. Buscar usuario")
        print("4. Borrar usuario")
        print("5. Salir")
        
        opcion = input("\nSelecciona (1-5): ").strip()

        match opcion:
            case "1":
                nombre = input("Nombre: ").strip()
                try:
                    edad = int(input("Edad: "))
                    user = {"nombre": nombre, "edad": edad, "es_adulto": es_mayor_de_edad(edad)}
                    usuarios = cargar_datos()
                    usuarios.append(user)
                    guardar_datos(usuarios)
                    print("✅ Guardado.")
                except ValueError:
                    print("❌ Edad inválida.")
            case "2":
                # Aquí podrías reusar tu función de listar anterior
                print(cargar_datos()) 
            case "3":
                buscar_usuario()
            case "4":
                borrar_usuario()
            case "5":
                print("👋 ¡Adiós!")
                break
            case _:
                print("⚠️ Opción inválida.")

if __name__ == "__main__":
    menu_principal()