import re
# Se importa la clase Contacto
from definirclase import Contacto 

# Validador de expresiones regulares
def RegEx(_txt,_regex):
    coincidencia=re.match(_regex, _txt)
    return bool(coincidencia)

# Expresiones regulares para cada campo.
NICKNAMERegEx="^[A-Z0-9]{5,15}$"
NOMBRERegEx="^[A-Z]+(([',. -][A-Z ])?[A-Z]*)*$"
CORREORegEs="^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
TELEFONORegEx="^[0-9]{2} [0-9]{4} [0-9]{4}"
FECHANACIMIENTORegEx="^[0-9]{4}/[0-9]{2}/[0-9]{2}$"
GASTORegEx="^[-+]?\d*\.?\d*$"
entidadValida=True               

def principal():
    while (True):
        LimpiarPantalla()
        print("LISTA DE COTACTOS")
        print(" ")
        print("[1] Agregar un contacto.")
        print("[2] Buscar un contacto.")
        print("[3] Eliminar un contacto.")
        print("[4] Mostrar contactos.")
        print("[5] Serializar datos.")
        print("[0] Salir.")
        opcion_elegida = input("¿Qué deseas hacer?  > ")
        if RegEx(opcion_elegida,"^[123450]{1}$"):
            if opcion_elegida=="0":
                print("GRACIAS POR UTILIZAR EL PROGRAMA")
                break
            if opcion_elegida=="1":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="2":
                print("Seleccionaste la Opcion Buscar Contacto")
                Telefono=int(input("Ingresa Telefono a Buscar: "))

                indice_obtenido=BuscarContacto(Telefono)
                if indice_obtenido==-1:
                    print("No se encontró el objeto")
                else:
                    print(Contactos[indice_obtenido].TELEFONO)
                    print(Contactos[indice_obtenido].NOMBRE)
                    print(Contactos[indice_obtenido].CORREO)

            if opcion_elegida=="3":
                print("Llamar procedimiento para la acción")
            if opcion_elegida=="4":
                print("Mostrando Contactos")
                # Ordenamiento.
                Contactos.sort(key=attrgetter("TELEFONO"),reverse=False)
                # Barrido secuencial.
                for contacto in Contactos:
                    print("------------------------------------------")
                    print(contacto.NICKNAME)
                    print(contacto.NOMBRE)
                    print(contacto.CORREO)
                    print(contacto.TELEFONO)
                    print(contacto.FECHANACIMIENTO)
                    print(contacto.GASTO)
            if opcion_elegida=="5":
                print("Llamar procedimiento para la acción")

            input("Pulsa enter para contunuar...")
        else:
            print("Esa respuesta no es válida.")
            input("Pulsa enter para contunuar...")

principal()
