import csv
# Librería para manejar datos de tipo datetime
import datetime

# Clase para almacenar los incidentes
class  Contacto:
      def __init__(self,NICKNAME,NOMBRE,CORREO,TELEFONO,FECHANACIMIENTO,GASTOS):
            self.NICKNAME = NICKNAME
            self.NOMBRE = NOMBRE
            self.CORREO = CORREO
            self.TELEFONO = TELEFONO
            self.FECHANACIMIENTO = FECHANACIMIENTO
            self.GASTOS = GASTOS
                        
# Lectura secuencial del archivo
with open('contactos_mobil.csv') as archivo_csv:
    lector_csv = csv.reader(archivo_csv, delimiter='|')
    contador_lineas = 0
    # Creando una lista vacía.
    lista_contactos = []
    # Lectura secuencial.
    for linea_datos in lector_csv:
        if contador_lineas == 0:
           
            print(f'Los nombres de columna son {", ".join(linea_datos)}')
        else:
            
            objeto_temporal = Incidente({linea_datos[0]},{linea_datos[1]},{linea_datos[2]},{linea_datos[3]})
            lista_contactos.append(objeto_temporal)

        contador_lineas += 1

    print(f'Procesadas {len(lista_contactos)} líneas.')

