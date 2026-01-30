import json
import os
# Importamos colorama
from colorama import Fore, Style, init

# Inicializamos colorama (autoreset=True hace que el color vuelva a la normalidad tras cada print)
init(autoreset=True)

def es_mayor_de_edad(edad: int) -> bool:
    return edad >= 18

def cargar_datos(filename: str = "usuarios.json") -> list:
    if not os.path.exists(filename):
        return []
    with open(filename, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def guardar_datos(usuarios: list, filename: str = "usuarios.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(usuarios, f, indent=4, ensure_ascii=False)

# --- CRUD CON COLORES ---

def buscar_usuario():
    query = input(f"{Fore.CYAN}🔍 Introduce el nombre a buscar: ").strip().lower()
    usuarios = cargar_datos()
    resultados = [u for u in usuarios if query in u["nombre"].lower()]
    
    if not resultados:
        print(f"\n{Fore.RED}❌ No se encontraron resultados para: '{query}'")
    else:
        print(f"\n{Fore.GREEN}✅ Se encontraron {len(resultados)} coincidencias:")
        for u in resultados:
            print(f"{Fore.YELLOW}- {u['nombre']} {Fore.WHITE}({u['edad']} años)")

def borrar_usuario():
    nombre_a_borrar = input(f"{Fore.CYAN}🗑️ Nombre exacto del usuario a eliminar: ").strip()
    usuarios = cargar_datos()
    nueva_lista = [u for u in usuarios if u["nombre"] != nombre_a_borrar]
    
    if len(nueva_lista) == len(usuarios):
        print(f"\n{Fore.YELLOW}⚠️ No se encontró a '{nombre_a_borrar}'. Nada que borrar.")
    else:
        guardar_datos(nueva_lista)
        print(f"\n{Fore.GREEN}✨ Usuario '{nombre_a_borrar}' eliminado correctamente.")

def menu_principal():
    while True:
        print("\n" + Fore.BLUE + "═"*30)
        print(Fore.BLUE + Style.BRIGHT + " 🚀 SISTEMA DE GESTIÓN CRUD")
        print(Fore.BLUE + "═"*30)
        print(f"{Fore.WHITE}1. Registrar usuario")
        print(f"{Fore.WHITE}2. Listar todos")
        print(f"{Fore.WHITE}3. Buscar usuario")
        print(f"{Fore.WHITE}4. Borrar usuario")
        print(f"{Fore.RED}5. Salir")
        
        opcion = input(f"\n{Fore.YELLOW}Selecciona (1-5): ").strip()

        match opcion:
            case "1":
                nombre = input("Nombre: ").strip()
                try:
                    edad = int(input("Edad: "))
                    user = {"nombre": nombre, "edad": edad, "es_adulto": es_mayor_de_edad(edad)}
                    usuarios = cargar_datos()
                    usuarios.append(user)
                    guardar_datos(usuarios)
                    print(f"{Fore.GREEN}✅ Guardado correctamente.")
                except ValueError:
                    print(f"{Fore.RED}❌ Error: Edad inválida.")
            case "2":
                print(f"\n{Fore.MAGENTA}--- LISTA DE USUARIOS ---")
                print(cargar_datos()) 
            case "3":
                buscar_usuario()
            case "4":
                borrar_usuario()
            case "5":
                print(f"{Fore.CYAN}👋 ¡Adiós!")
                break
            case _:
                print(f"{Fore.RED}⚠️ Opción inválida.")

if __name__ == "__main__":
    menu_principal()