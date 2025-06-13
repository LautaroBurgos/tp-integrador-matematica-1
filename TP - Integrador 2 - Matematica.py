# A. Operaciones con DNIs
print("-----A. Operaciones con DNIs-----")
print("Ingresando DNIs de los jugadores... ")

dniAlumnos = {
    'martinez': "32845647",
    'otamendi': "31155789",
    'macallister': "38456127",
    'fernandez': "42574621",
    'depaul': "41245678",
    'alvarez': "42978465"
}

for apellido, dni in dniAlumnos.items():
    print(f"{str.capitalize(apellido)}: {dni}")

print("\nGeneración de los conjuntos de dígitos únicos...")
conjuntosDniAlumnos = {}
for apellido, dni in dniAlumnos.items():
    conjuntosDniAlumnos[apellido] = set(dni)

for apellido, conjunto in conjuntosDniAlumnos.items():
    print(f"{str.capitalize(apellido)}: {conjunto}")

def sumaDigitosDni(dni):
    return sum(int(d) for d in dni)

def interseccionConjuntos(c1, c2):
    return list(set(c1).intersection(c2))

def menuUnion(conjuntosDniAlumnos):
    def unionConjuntos(c1, c2):
        return list(set(c1).union(c2))

    print("\n-----1 - Unión de conjuntos-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == 'martinez':
            continue
        print(f"Unión de Martinez y {str.capitalize(apellido)}: {unionConjuntos(conjuntosDniAlumnos['martinez'], conjunto)}")

def menuInterseccion(conjuntosDniAlumnos):
    print("\n-----2 - Intersección de conjuntos-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == 'martinez':
            continue
        print(f"Intersección de Martinez y {str.capitalize(apellido)}: {interseccionConjuntos(conjuntosDniAlumnos['martinez'], conjunto)}")

def menuDiferencia(conjuntosDniAlumnos):
    def diferenciaEntrePares(c1, c2):
        return list(set(c1) - set(c2))

    print("\n-----3 - Diferencia entre pares de conjuntos-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == 'martinez':
            continue
        print(f"Diferencia de Martinez y {str.capitalize(apellido)}: {diferenciaEntrePares(conjuntosDniAlumnos['martinez'], conjunto)}")

def menuDiferenciaSimetrica(conjuntosDniAlumnos):
    def diferenciaSimetrica(c1, c2):
        return list(set(c1).symmetric_difference(c2))

    print("\n-----4 - Diferencia simétrica-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == 'martinez':
            continue
        print(f"Diferencia simétrica entre Martinez y {str.capitalize(apellido)}: {diferenciaSimetrica(conjuntosDniAlumnos['martinez'], conjunto)}")

def menuFrecuencia(dniAlumnos):
    def contarFrecuenciaDni(dni):
        freq = {}
        for d in dni:
            freq[d] = freq.get(d, 0) + 1
        return freq

    print("\n-----5 - Frecuencia de cada dígito en los DNI-----")
    for apellido, dni in dniAlumnos.items():
        frec = contarFrecuenciaDni(dni)
        for digito, count in sorted(frec.items()):
            print(f"{str.capitalize(apellido)} - Dígito {digito}: {count} vez/veces")
        print()

def menuSumaDigitos(dniAlumnos):
    print("\n-----6 - Suma total dígitos DNI-----")
    for apellido, dni in dniAlumnos.items():
        print(f"Suma de los dígitos del DNI de {str.capitalize(apellido)}: {sumaDigitosDni(dni)}")

def menuDigitoCompartido(conjuntosDniAlumnos):
    print("\n-----7 - Evaluación lógica: Dígito compartido-----")
    inter = set.intersection(*[set(v) for v in conjuntosDniAlumnos.values()])
    print("Dígitos compartidos entre todos:", list(inter))

def menuDiversidadAlta(conjuntosDniAlumnos):
    print("\n-----8 - Evaluación lógica: Diversidad numérica-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        tipo = "Alta" if len(conjunto) > 6 else "Baja"
        print(f"DNI de {str.capitalize(apellido)}: Diversidad Numérica {tipo}")

def menuSumaTotalDigitosDni(dniAlumnos):
    print("\n-----9 - Evaluación lógica: Suma total de dígitos repetida-----")
    sumaDict = {}
    for apellido, dni in dniAlumnos.items():
        s = sumaDigitosDni(dni)
        sumaDict.setdefault(s, []).append(apellido)
    for suma, apellidos in sumaDict.items():
        if len(apellidos) > 1:
            print(f"Suma {suma}: {', '.join(apellidos)}")

def menuCompatibilidadDnis(conjuntosDniAlumnos):
    print("\n-----10 - Compatibilidad entre conjuntos de DNIs-----")
    def altaCompatibilidad(n1, c1, n2, c2):
        comunes = interseccionConjuntos(c1, c2)
        nivel = "alta" if len(comunes) >= 3 else "baja"
        return f"{n1} tiene {nivel} compatibilidad con {n2}"
    print(altaCompatibilidad("Martinez", conjuntosDniAlumnos['martinez'], "Otamendi", conjuntosDniAlumnos['otamendi']))

# B. Operaciones con años de nacimiento
aniosNacimiento = {
    "Martinez": 1992,
    "Otamendi": 1988,
    "Macallister": 1998,
    "Fernandez": 2001,
    "Depaul": 1994,
    "Alvarez": 2000
}
listaAnios = list(aniosNacimiento.values())

def menuCantAniosParesImpares(listaAnios):
    pares = sum(1 for a in listaAnios if a % 2 == 0)
    impares = len(listaAnios) - pares
    print("\n-----11 - Cantidad de años pares e impares-----")
    print(f"Pares: {pares} - Impares: {impares}")

def menuGrupoZoBoomers(listaAnios):
    print("\n-----12 - Grupo Z u Old School-----")
    grupo = "Z" if all(a > 2000 for a in listaAnios) else "Old School"
    print(f"Tenemos un grupo {grupo}")

def menuVerificaBisiesto(listaAnios):
    print("\n-----13 - Verifica año bisiesto-----")
    for a in listaAnios:
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print(f"Año especial: {a}")
            break

def menuProdCartesianoAniosEdades(aniosNacimiento):
    print("\n-----14 - Producto cartesiano años y edades-----")
    anioActual = 2025
    for nombre, anio in aniosNacimiento.items():
        edad = anioActual - anio
        print(f"{nombre} nació en {anio} y tiene {edad} años.")

# Menú principal (comentado para evitar ejecución automática)
################## MENU #############################
opciones = {
    '1': lambda: menuUnion(conjuntosDniAlumnos),
    '2': lambda: menuInterseccion(conjuntosDniAlumnos),
    '3': lambda: menuDiferencia(conjuntosDniAlumnos),
    '4': lambda: menuDiferenciaSimetrica(conjuntosDniAlumnos),
    '5': lambda: menuFrecuencia(dniAlumnos),
    '6': lambda: menuSumaDigitos(dniAlumnos),
    '7': lambda: menuDigitoCompartido(conjuntosDniAlumnos),
    '8': lambda: menuDiversidadAlta(conjuntosDniAlumnos),
    '9': lambda: menuSumaTotalDigitosDni(dniAlumnos),
    '10': lambda: menuCompatibilidadDnis(conjuntosDniAlumnos),
    '11': lambda: menuCantAniosParesImpares(listaAnios),
    '12': lambda: menuGrupoZoBoomers(listaAnios),
    '13': lambda: menuVerificaBisiesto(listaAnios),
    '14': lambda: menuProdCartesianoAniosEdades(aniosNacimiento)
}
while True:
    print("\n-------------------TP SEMANA DE INTEGRACION II - MENU-------------------")
    print("--- A. Operaciones con DNIs ---")
    print("1 - Union de conjuntos")
    print("2 - Intersección de conjuntos")
    print("3 - Diferencia entre pares de conjuntos")
    print("4 - Diferencia simétrica")
    print("5 - Frecuencia de cada dígito en los DNI")
    print("6 - Suma total dígitos DNI")
    print("7 - Evaluacion lógica: Dígito compartido")
    print("8 - Evaluacion lógica: Diversidad numérica")
    print("9 - Evaluacion lógica: Pares de dni con mismo valor en la suma de sus dígitos")
    print("10 - Compatibilidad entre conjuntos de DNI")
    print("--- B. Operaciones con años de nacimiento ---")
    print("11 - Cantidad de años pares e impares")
    print("12 - Grupo Z o Boomers")
    print("13 - Verifica año bisiesto")
    print("14 - Producto cartesiano entre años y edades")
    print("0 - Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == '0':
        break

    if opcion in opciones:
        opciones[opcion]()
        print("\n-------------------------------------")
        print(input("(presione cualquier tecla para volver al menu)"))