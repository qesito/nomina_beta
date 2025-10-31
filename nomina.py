nomina = [
    [100,"José Pérez Ramos", "Producción", "Obrero", 7, 825, 9, 200, 0, 0],
    [110,"Pablo Ramírez Ruiz", "Producción", "Obrero", 7, 825, 10, 200, 0, 0],
    [130,"Ma. Luz Aguilar Hernández", "Producción", "Obrero", 7, 825, 12, 200, 0, 0],
    [135,"Roberto Haro Torres", "Ventas", "Empleado", 15, 955, 10, 250, 0, 0],
    [143,"Rosa López Juárez", "Ventas", "Empleado", 15, 955, 4, 250, 0, 0],
    [150,"Ramón Martínez Suarez", "Ventas", "Empleado", 15, 955, 9, 250, 0, 0],
    [163,"Santiago Alonso Contreras", "Compras", "Empleado", 15, 955, 11, 250, 0, 0],
    [174,"Jesús Campos Sánchez", "Compras", "Empleado", 15, 955, 11, 250, 0, 0],
    [183,"Moisés Castro Montante", "Compras", "Empleado", 15, 955, 0, 250, 0, 0],
    [192,"Pablo Cervantes Salinas", "Recursos Humanos", "Empleado", 15, 955, 6, 250, 0, 0],
    [203,"Anahí Torres Carreón", "Recursos Humanos", "Empleado", 15, 955, 3, 250, 0, 0],
    [213,"Nuria Lira González", "Recursos Humanos", "Empleado", 15, 955, 0, 250, 0, 0],
    [226,"Miguel Mendoza Sánchez", "Producción", "Empleado", 7, 825, 1, 200, 0, 0],
    [234,"Sofia González Esparza", "Dirección", "Directivo", 15, 2000, 0, 0, 800, 0],
    [241,"Cristian González González", "Producción", "Obrero", 7, 825, 6, 200, 0, 0],
    [255,"Juan Gámez Aguilar", "Ventas", "Empleado", 15, 955, 8, 250, 0, 0],
    [261,"Fernando López Nuño", "Dirección", "Empleado", 15, 1200, 1, 250, 0, 0],
    [274,"Abraham Lozano De Lira", "Compras", "Empleado", 15, 955, 8, 250, 0, 0],
    [283,"Ángel Negrete Demetrio", "Ventas", "Empleado", 15, 955, 1, 250, 0, 0],
    [294,"Damián Nieves Quezada", "Recursos Humanos", "Empleado", 15, 955, 10, 250, 0, 0],
    [307,"Armando Reyes Martínez", "Compras", "Empleado", 15, 955, 8, 250, 0, 0],
    [318,"Manuel Ruiz Mendoza", "Ventas", "Empleado", 15, 955, 3, 250, 0, 0],
    [326,"Esteban Salado Muñoz", "Dirección", "Directivo", 15, 1500, 0, 0, 1000, 0],
    [331,"Alejandro Soto Ocampo", "Dirección", "Directivo", 15, 1200, 0, 0, 1200, 0],
    [337,"Alondra Valdés Mora", "Dirección", "Directivo", 15, 1200, 0, 0, 2000, 0],
]

cabeceras = [
    "No. de Trabajador", "Nombre", "Departamento", "Tipo de Empleado",
    "Días Trabajados", "Pago Diario", "Horas Extra", "Pago por Hora Extra", "Sueldo Bruto" , "Bono Productividad"
]

inx = {
    "no_trab": 0, "nombre": 1, "dpto": 2, "tipo": 3, 
    "dias": 4, "pago_dia": 5, "h_extra": 6, "pago_h_extra": 7, "bono_prod": 8 ,"sueldo_bruto": 9, 
    }
def mostrar_menu_principal(): #chuy
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

def encontrar_empleado(num_trabajador):#fer
    for i, empleado in enumerate(nomina):
        if empleado[0] == num_trabajador:
            return i, empleado
    return None,None
#def mostrar_tabla_empleados():
def mostrar_tabla_empleados():#emiliano
    """Muestra la nómina básica con formato de texto fijo."""
    print("\n--- LISTA DE TRABAJADORES ---")
    # Imprime encabezados
    print(f"{'No.':<8} {'Nombre':<35}")
    
    for empleado in nomina:
        print(f"{empleado[inx['no_trab']]:<8} {empleado[inx['nombre']]:<35}")
    
def pedir_numero_isdigit(mensaje):#fer
    while True:
        valor_str = input(mensaje)
        if valor_str.isdigit():
            return int(valor_str)
        else:
            print("Error: Debe ingresar un valor numérico positivo.")

def menu_cambio():#fer
    while True: 
        mostrar_tabla_empleados()
        
        empleado_cambio = pedir_numero_isdigit("\nIngresa el número de empleado a cambiar: ")

        empleado_datos = encontrar_empleado(empleado_cambio)
        
        if empleado_datos[1] is not None:
            
            indice_empleado = empleado_datos[0] 
            
            while True:
                datos_actuales = nomina[indice_empleado]
                
                print("\n--- Modificando a:", datos_actuales[inx['nombre']], "---")
                print(f" 1-No. Trabajador: {datos_actuales[inx['no_trab']]}")
                print(f" 2-Nombre: {datos_actuales[inx['nombre']]}")
                print(f" 3-Departamento: {datos_actuales[inx['dpto']]}")
                print(f" 4-Tipo de Empleado: {datos_actuales[inx['tipo']]}")
                print(f" 5-Días Trabajados: {datos_actuales[inx['dias']]}")
                print(f" 6-Pago Diario: {datos_actuales[inx['pago_dia']]}")
                print(f" 7-Horas Extra: {datos_actuales[inx['h_extra']]}")
                print(f" 8-Pago por Hora Extra: {datos_actuales[inx['pago_h_extra']]}")
                print(f" 9-Bono productividad: {datos_actuales[inx['bono_prod']]}")
                print("\n 10-Salir")
                
                cambio = pedir_numero_isdigit("\nIngresa el numero del dato a cambiar: ")
                
                if cambio == 1:
                    nuevo_dato = pedir_numero_isdigit("\nIngrese el nuevo numero del trabajador: ")
                    nomina[indice_empleado][inx['no_trab']] = nuevo_dato
                
                elif cambio == 2:
                    nuevo_dato = input("Ingrese el nuevo nombre del trabajador: ")
                    nomina[indice_empleado][inx['nombre']] = nuevo_dato
                
                elif cambio == 3:
                    nuevo_dato = input("Ingrese el nuevo departamento del trabajador:  ")
                    nomina[indice_empleado][inx['dpto']] = nuevo_dato
                
                elif cambio == 4:
                    nuevo_dato = input("Ingrese el nuevo tipo de empleado: ")
                    nomina[indice_empleado][inx['tipo']] = nuevo_dato
                
                elif cambio == 5:
                    nuevo_dato = pedir_numero_isdigit("Ingrese los nuevos dias trabajados: ")
                    nomina[indice_empleado][inx['dias']] = nuevo_dato
                
                elif cambio == 6:
                    nuevo_dato = pedir_numero_isdigit("Ingrese el nuevo pago diario: ")
                    nomina[indice_empleado][inx['pago_dia']] = nuevo_dato
                
                elif cambio == 7: 
                    nuevo_dato = pedir_numero_isdigit("Ingrese las nuevas horas extras: ")
                    nomina[indice_empleado][inx['h_extra']] = nuevo_dato
                
                elif cambio == 8: 
                    nuevo_dato = pedir_numero_isdigit("Ingrese el nuevo pago por hora extra: ")
                    nomina[indice_empleado][inx['pago_h_extra']] = nuevo_dato
                
                elif cambio == 9: 
                    nuevo_dato = pedir_numero_isdigit("Ingrese el nuevo bono productividad: ")
                    nomina[indice_empleado][inx['bono_prod']] = nuevo_dato

                elif cambio == 10:
                    print("Guardando cambios y saliendo...")
                    nomina.sort() 
                    return 
                else:
                    print("Opción inválida. Intente de nuevo (1-10).")
        else:
            print(f"\nEl número de trabajador {empleado_cambio} no existe. Intente de nuevo.")
        
# 𝑆𝑢𝑒𝑙𝑑𝑜 = 𝐷í𝑎𝑠 𝑇𝑟𝑎𝑏𝑎𝑗𝑎𝑑𝑜𝑠 ∗ 𝑃𝑎𝑔𝑜 𝐷𝑖𝑎𝑟𝑖𝑜 + 𝐻𝑜𝑟𝑎𝑠 𝐸𝑥𝑡𝑟𝑎 ∗ 𝑃𝑎𝑔𝑜 𝑝𝑜𝑟 𝐻𝑜𝑟𝑎 𝐸𝑥𝑡𝑟𝑎 + 𝐵𝑜𝑛𝑜 𝑃𝑟𝑜𝑑𝑢𝑡𝑖𝑣𝑖𝑑𝑎𝑑
def calcular_sueldos():#emiliano
    for i, empleado in enumerate(nomina):
        sueldo_diario = empleado[inx["dias"]] * empleado[inx["pago_dia"]]
        pago_extra = empleado[inx["h_extra"]] * empleado[inx["pago_h_extra"]]
        sueldo_bruto = sueldo_diario + pago_extra + empleado[inx["bono_prod"]]
        
        nomina[i][inx["sueldo_bruto"]] = round(sueldo_bruto, 2)
            

def desplegar_sueldos():#emiliano
    print("\n--- TABLA DE SUELDOS ---")
    # Imprime encabezados
    print(f"{'No.':<8} {'Nombre':<35} {'Departamento':<15} {'Tipo de Empleado':<15} {'Días trabajados':<8} {'Pago Diario':<10} {'Horas Extra':<10} {'Pago por hora extra':<10} {'Bono Productividad':15} {'Sueldo Bruto':<10}")
    print("-" * 150)
    
    for empleado in nomina:
        print(f"{empleado[inx['no_trab']]:<8} {empleado[inx['nombre']]:<35} {empleado[inx['dpto']]:<15} {empleado[inx['tipo']]:<15} {empleado[inx['dias']]:<8} {empleado[inx['pago_dia']]:<10} {empleado[inx['h_extra']]:<10} {empleado[inx['pago_h_extra']]:<10} {empleado[inx['bono_prod']]:<15} ${empleado[inx['sueldo_bruto']]:<10,.2f}")
    
def sueldo_departamento():#rita
    total_dpto = {}
    for empleado in nomina:
        departamento = empleado[inx["dpto"]]
        sueldo = empleado[inx["sueldo_bruto"]]

        if departamento in total_dpto:
            total_dpto[departamento] += sueldo
        else:
            total_dpto[departamento] = sueldo

    print("\n--- Sueldos totales por departamento---")
    for dpto, total in total_dpto.items(): #.items devuelve pares clave-valor de un diccionario
        print(f"{dpto:<15}: ${total:,.2f}") #<- dpto:<15 va a alinear, :$ signo de pesos, ,.2f dos decimales


def sueldo_empleado():#rita
    total_tipo = {}
    for empleado in nomina:
        tipo = empleado[inx["tipo"]]
        sueldo = empleado[inx["sueldo_bruto"]]

        if tipo in total_tipo:
            total_tipo[tipo] += sueldo
        else:
            total_tipo[tipo] = sueldo

    print("\n--- Sueldos por tipo de empleado---")
    for tipo, total in total_tipo.items(): 
        print(f"{tipo:<15}: ${total:,.2f}") 

def sueldos_horasx():#rita
    total_pbase = 0.0
    total_pextra = 0.0
    total_pbono = 0.0

    for empleado in nomina:
        pbase = empleado[inx["dias"]] * empleado[inx["pago_dia"]]
        total_pbase += pbase

        pextra = empleado[inx["h_extra"]] * empleado[inx["pago_h_extra"]]
        total_pextra += pextra
        bono_act = empleado[inx["bono_prod"]]
        total_pbono += bono_act
        totalgral = total_pextra + total_pbase + total_pbono
    
    print(f"{'Total sueldos':<15} | ${total_pbase:<9,.2f}")
    print(f"{'Total horas extra':<15} | ${total_pextra:<9,.2f}")
    print(f"{'Total bonos de productividad':<15} | ${total_pbono:<9,.2f}")
    print(f"{'Total':<15} |${totalgral:<9,.2f}")
    
#funcion principal de ejecucion 

def main():#fer
    calcular_sueldos()
    while True:
        opcion = mostrar_menu_principal()
        if opcion == '1':
            calcular_sueldos()
            menu_cambio()
        elif opcion == '2':
            calcular_sueldos()
            print(f"\nSe calcularon sueldos")
        elif opcion == '3':
            calcular_sueldos()
            desplegar_sueldos()
        elif opcion == '4':
            calcular_sueldos()
            sueldo_departamento()
        elif opcion == '5':
            calcular_sueldos()
            sueldo_empleado()
        elif opcion == '6':
            calcular_sueldos()
            sueldos_horasx()
        elif opcion == '7':
            print("Saliendo del programa. Hasta pronto")
            break
        else:
            print("Opción no válida. Por favor, seleccione un número del 1 al 7.")
            
if __name__ == "__main__":#chuy
    main()