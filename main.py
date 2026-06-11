from calculos import es_surfeable,alertar_viento_peligroso,obtener_temperatura_limite_traje,mostrar_advertencia_marejada
from pantalla import mostrar_titulo,titulo_menu

def menu():
    mostrar_titulo()
    altura_ola = float(input("Ingrese la altura de las olas en metros: "))
    viento = int(input("Ingrese la velocidad del viento en nudos"))
    while True:
        titulo_menu()
        print(f"OLA Ingresada: {altura_ola}metros | Viento: {viento} nudos")
        print("1.- ¿Es surfeable hoy?")
        print("2.- Evaluar peligro de viento")
        print("3.- Consultar límite de temperatura")
        print("4.- Ver aviso de la armada")
        print("5.- Actualizar datos")
        print("6.- Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            apto = es_surfeable(altura_ola)
            if apto: 
                print("Excelentes olas para el surf")
            else:
                print("El mar está muy tranquilo")
        elif opcion == "2":
            alertar_viento_peligroso(viento)
        elif opcion == "3":
            temp_critica = obtener_temperatura_limite_traje()
            print(f"Recuerda: bajo los {temp_critica}°C es obligatorio usar traje 4/3mm")
        elif opcion == "4":
            mostrar_advertencia_marejada()
        elif opcion == "5":
            altura_ola = float(input("Ingresa la nueva altura de olas en metros: "))
            viento = int(input("Ingresa la nueva velocidad del viento en nudos: "))
            print("[INFO]: Datos actualizados")
        elif opcion == "6":
            print("Saliendo del sistema ....")
            break
        else:
            print("Opción no válida")
if __name__ == "__main__":
    menu()
        