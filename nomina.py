#!/usr/bin/env python3

# autores: qesito, emilianosdev, vtorrres

import numpy as np


nomina = [
    [100,"jose perez ramos", "produccion", "obrero", 7, 825, 9, 200],
    [110,"Pablo ramirez ruiz", "produccion", "obrero", 7, 825, 10, 200],
    [130,"Ma. Luz Aguilar Hernández", "Producción", "Obrero", 7, 825, 12, 200],
    [135,"Roberto Haro Torres", "Ventas", "Empleado", 15, 955, 10, 250],
    [143,"Rosa López Juárez", "Ventas", "Empleado", 15, 955, 4, 250],
    [150,"Ramón Martínez Suarez", "Ventas", "Empleado", 15, 955, 9, 250],
    [163,"Santiago Alonso Contreras", "Compras", "Empleado", 15, 955, 11, 250],
    [174,"Jesús Campos Sánchez", "Compras", "Empleado", 15, 955, 11, 250],
    [183,"Moisés Castro Montante", "Compras", "Empleado", 15, 955, 0, 250],
    [192,"Pablo Cervantes Salinas", "Recursos Humanos", "Empleado", 15, 955, 6, 250],
    [203,"Anahí Torres Carreón", "Recursos Humanos", "Empleado", 15, 955, 3, 250],
    [213,"Nuria Lira González", "Recursos Humanos", "Empleado", 15, 955, 0, 250],
    [226,"Miguel Mendoza Sánchez", "Producción", "Empleado", 7, 825, 1, 200],
    [234,"Sofia González Esparza", "Dirección", "Directivo", 15, 2000, 0, None],
    [241,"Cristian González González", "Producción", "Obrero", 7, 825, 6, 200],
    [255,"Juan Gámez Aguilar", "Ventas", "Empleado", 15, 955, 8, 250],
    [261,"Fernando López Nuño", "Dirección", "Empleado", 15, 1200, 1, 250],
    [274,"Abraham Lozano De Lira", "Compras", "Empleado", 15, 955, 8, 250],
    [283,"Ángel Negrete Demetrio", "Ventas", "Empleado", 15, 955, 1, 250],
    [294,"Damián Nieves Quezada", "Recursos Humanos", "Empleado", 15, 955, 10, 250],
    [307,"Armando Reyes Martínez", "Compras", "Empleado", 15, 955, 8, 250],
    [318,"Manuel Ruiz Mendoza", "Ventas", "Empleado", 15, 955, 3, 250],
    [326, "Esteban Salado Muñoz", "Dirección", "Directivo", 15, 1500, 0, None],
    [331, "Alejandro Soto Ocampo", "Dirección", "Directivo", 15, 1200, 0, None],
    [337,"Alondra Valdés Mora", "Dirección", "Directivo", 15, 1200, 0, None],
]

cabeceras = [
    "No. de Trabajador", "Nombre", "Departamento", "Tipo de Empleado",
    "Días Trabajados", "Pago Diario", "Horas Extra", "Pago por Hora Extra", "Sueldo Bruto"
]

inx = {
    "no_trab": 0, "nombre": 1, "dpto": 2, "tipo": 3, 
    "dias": 4, "pago_dia": 5, "h_extra": 6, "pago_h_extra": 7, "sueldo_bruto": 8
}

def mostrar_menu_principal():
    print("\n--- Menú ---")
    print("1.- Modificar información")
    print("2.- Calcula sueldos")
    print("3.- Despliega sueldos")
    print("4.- Sueldos por Departamentos")
    print("5.- Sueldos por tipo de Empleado")
    print("6.- Sueldos y Horas Extra")
    print("7.- Salir")
    opcion = input("Seleccione una opción: ")
    return opcion

def encontrar_empleado(num_trabajador):
    for i, empleado in enumerate(nomina):
        if empleado[0] == num_trabajador:
            return i, empleado
    return None


def mostrar_tabla_empleados():
    for i in range(len(nomina)):
        print("\n No. Trabajador", nomina[i][0], "\n Nombre:", nomina[i][1], "\n Departamento:", nomina[i][2], "\n Tipo de Empleado:", nomina[i][3], "\n Días Trabajados:", nomina[i][4], "\n Pago Diario:", nomina[i][5], "\n Horas Extra:", nomina[i][6], "\n Pago por Hora Extra:", nomina[i][7])
    
    
def menu_cambio():
    mostrar_tabla_empleados()
    empleado_cambio = int(input("ingresa el numero de empleado a cambiar: "))
    empleado_datos = encontrar_empleado(empleado_cambio)
    print("\n 1-No. Trabajador", empleado_datos[1][0], "\n 2-Nombre:", empleado_datos[1][1], "\n 3-Departamento:", empleado_datos[1][2], "\n 4-Tipo de Empleado:", empleado_datos[1][3], "\n 5-Días Trabajados:", empleado_datos[1][4], "\n 6-Pago Diario:", empleado_datos[1][5], "\n 7-Horas Extra:", empleado_datos[1][6], "\n 8-Pago por Hora Extra:", empleado_datos[1][7],"\n 9-Salir")
    cambio = int(input("ingresa el numero del dato a cambiar: "))
    if cambio == 1:
        nuevo_dato = int(input("ingrese el nuevo numero de trabajador: "))
        nomina[empleado_datos[0]][0] = nuevo_dato
    elif cambio == 2:
        nuevo_dato = input("ingrese el nuevo nombre de trabajador: ")
        nomina[empleado_datos[0]][1] = nuevo_dato


def calcular_sueldos():
    for i, empleado in enumerate(nomina):
        sueldo_diario = empleado[inx["dias"]] * empleado[inx["pago_dia"]]
        pago_extra = empleado[inx["h_extra"]] * empleado[inx["pago_h_extra"]]
        sueldo_bruto = sueldo_diario + pago_extra

        nomina[i]["sueldo_bruto"] = round(sueldo_bruto, 2)
        print(f"Sueldo de {empleado[inx['nombre']]} ({empleado[inx['no_trab']]}) calculado: ${sueldo_bruto:.2f}")


#funcion principal de ejecucion dios mio ayudame:

def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1':
            menu_cambio()
        elif opcion == '2':
            calcular_sueldos()
        elif opcion == '3':
            print("eso roni")
        elif opcion == '4':
            pass
        elif opcion == '5':
            pass
        elif opcion == '6':
            pass
        elif opcion == '7':
            print("Saliendo del programa. Hasta pronto")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 7.")
            
if __name__ == "__main__":
    main()
