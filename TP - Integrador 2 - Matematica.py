from datetime import datetime # Para sacar el anio en curso
from itertools import product # Producto cartesiano

ALUMNOS = {
    'burgos': {"dni": "42575853", "anio": 2000},
    'bonelli': {"dni": "30654105", "anio": 1983},
    'borda': {"dni": "42684197", "anio": 2000},
    'bareiro': {"dni": "39316336", "anio": 1995}
}
APELLIDOS = list(ALUMNOS.keys())
ANIOS = list(v.get('anio') for v in ALUMNOS.values())

# A. Operaciones con DNIs
print("-----A. Operaciones con DNIs-----")
print("Listando DNIs de los alumnos... ")
for apellido, datos in ALUMNOS.items():
    print(f"{str.capitalize(apellido)}: {datos}")

print("\nGenerando conjuntos de dígitos únicos a partir de los DNIs...")
conjuntosDniAlumnos = {}
for apellido, datos in ALUMNOS.items():
    conjuntosDniAlumnos[apellido] = set(datos.get('dni'))

for apellido, conjunto in conjuntosDniAlumnos.items():
    print(f"{str.capitalize(apellido)}: {conjunto}")

def sumaDigitosDni(dni):
    return sum(int(d) for d in dni)

def interseccionConjuntos(c1, c2):
    return list(set(c1).intersection(c2))

def menuUnion(conjuntosDniAlumnos):
    def unionConjuntos(c1, c2):
        return list(set(c1).union(c2))
    apellidoSeleccion = None
    while True:
        print("\n-----1 - Unión de conjuntos-----")
        print("Conjuntos dispinibles: ")
        for i, k in enumerate(ALUMNOS.keys()):
            print(f"{i+1} - {str.capitalize(k)}")
        try:
            opcion = int(input("Seleccione el conjunto para unir: "))
            apellidoSeleccion = APELLIDOS[opcion - 1]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        break
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == apellidoSeleccion:
            continue
        print(f"Unión de {str.capitalize(apellidoSeleccion)} y {str.capitalize(apellido)}: {unionConjuntos(conjuntosDniAlumnos[apellidoSeleccion], conjunto)}")

def menuInterseccion(conjuntosDniAlumnos):
    apellidoSeleccion = None
    while True:
        print("\n-----2 - Intersección de conjuntos-----")
        print("\nConjuntos dispinibles: ")
        for i, k in enumerate(ALUMNOS.keys()):
            print(f"{i+1} - {str.capitalize(k)}")
        try:
            opcion = int(input("Seleccione el conjunto para interseccion: "))
            apellidoSeleccion = APELLIDOS[opcion - 1]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        break
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == apellidoSeleccion:
            continue
        print(f"Intersección de {str.capitalize(apellidoSeleccion)} y {str.capitalize(apellido)}: {interseccionConjuntos(conjuntosDniAlumnos[apellidoSeleccion], conjunto)}")

def menuDiferencia(conjuntosDniAlumnos):
    def diferenciaEntrePares(c1, c2):
        return list(set(c1) - set(c2))

    apellidoSeleccion = None
    while True:
        print("\n-----3 - Diferencia entre pares de conjuntos-----")
        print("\nConjuntos dispinibles: ")
        for i, k in enumerate(ALUMNOS.keys()):
            print(f"{i + 1} - {str.capitalize(k)}")
        try:
            opcion = int(input("Seleccione el conjunto para calcular diferencia: "))
            apellidoSeleccion = APELLIDOS[opcion - 1]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        break
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == apellidoSeleccion:
            continue
        print(f"Diferencia de {str.capitalize(apellidoSeleccion)} y {str.capitalize(apellido)}: {diferenciaEntrePares(conjuntosDniAlumnos[apellidoSeleccion], conjunto)}")

def menuDiferenciaSimetrica(conjuntosDniAlumnos):
    def diferenciaSimetrica(c1, c2):
        return list(set(c1).symmetric_difference(c2))
    while True:
        print("\n-----4 - Diferencia simétrica-----")
        print("\nConjuntos dispinibles: ")
        for i, k in enumerate(ALUMNOS.keys()):
            print(f"{i + 1} - {str.capitalize(k)}")
        try:
            opcion = int(input("Seleccione el conjunto para calcular diferencia simétrica: "))
            apellidoSeleccion = APELLIDOS[opcion - 1]
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        break
    for apellido, conjunto in conjuntosDniAlumnos.items():
        if apellido == apellidoSeleccion:
            continue
        print(f"Diferencia simétrica entre {str.capitalize(apellidoSeleccion)} y {str.capitalize(apellido)}: {diferenciaSimetrica(conjuntosDniAlumnos[apellidoSeleccion], conjunto)}")

def menuFrecuencia(alumnos):
    def contarFrecuenciaDni(dni):
        freq = {}
        for d in dni:
            freq[d] = freq.get(d, 0) + 1
        return freq

    print("\n-----5 - Frecuencia de cada dígito en los DNI-----")
    for apellido, datos in alumnos.items():
        dni = datos['dni']
        frec = contarFrecuenciaDni(dni)
        for digito, count in sorted(frec.items()):
            print(f"{str.capitalize(apellido)} - Dígito {digito}: {count} {"vez" if count == 1 else "veces"}")
        print()

def menuSumaDigitos(dniAlumnos):
    print("\n-----6 - Suma total dígitos DNI-----")
    for apellido, datos in dniAlumnos.items():
        print(f"Suma de los dígitos del DNI de {str.capitalize(apellido)}: {sumaDigitosDni(datos['dni'])}")

def menuDigitoCompartido(conjuntosDniAlumnos):
    print("\n-----7 - Evaluación lógica: Dígito compartido-----")
    inter = set.intersection(*[set(v) for v in conjuntosDniAlumnos.values()])
    if inter:
        print("Dígitos compartidos entre todos:", sorted(inter))
    else:
        print("No hay ningún dígito compartido entre todos los conjuntos.")

def menuDiversidadAlta(conjuntosDniAlumnos):
    print("\n-----8 - Evaluación lógica: Diversidad numérica-----")
    for apellido, conjunto in conjuntosDniAlumnos.items():
        tipo = "Alta" if len(conjunto) > 6 else "Baja"
        print(f"DNI de {str.capitalize(apellido)}: Diversidad Numérica {tipo}")

def menuSumaTotalDigitosDni(alumnos):
    print("\n-----9 - Evaluación lógica: Suma total de dígitos repetidos-----")
    sumaDict = {}
    repetidos = False
    for apellido, datos in alumnos.items():
        dni = datos['dni']
        s = sumaDigitosDni(dni)
        sumaDict.setdefault(s, []).append(apellido)
    for suma, apellidos in sumaDict.items():
        if len(apellidos) > 1:
            repetidos = True
            print(f"Suma {suma}: {', '.join(apellidos)}")
    if not repetidos:
        print("No se encontraron sumas repetidas entre los DNIs.")

def menuCompatibilidadDnis(conjuntosDniAlumnos):
    print("\n-----10 - Compatibilidad entre conjuntos de DNIs-----")
    def altaCompatibilidad(n1, c1, n2, c2):
        comunes = interseccionConjuntos(c1, c2)
        nivel = "alta" if len(comunes) >= 3 else "baja"
        return f"{n1} tiene {nivel} compatibilidad con {n2}"
    print(altaCompatibilidad("Bonelli", conjuntosDniAlumnos['bonelli'], "Burgos", conjuntosDniAlumnos['burgos']))

# B. Operaciones con años de nacimiento


def menuCantAniosParesImpares(listaAnios):
    pares = sum(1 for a in listaAnios if a % 2 == 0)
    impares = len(listaAnios) - pares
    print("\n-----11 - Cantidad de años pares e impares-----")
    print(f"Pares: {pares} - Impares: {impares}")

def menuGrupoZoBoomers(listaAnios):
    print("\n-----12 - Grupo Z o Boomer----")
    grupo = "Z" if all(a > 2000 for a in listaAnios) else "Boomer"
    print(f"Tenemos un grupo {grupo}")

def menuVerificaBisiesto(listaAnios):
    print("\n-----13 - Verifica año bisiesto-----")
    for a in listaAnios:
        if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
            print(f"Año especial: {a}")
            break

def menuProdCartesianoAniosEdades(alumnos):
    print("\n-----14 - Producto cartesiano años y edades-----")
    anioActual = datetime.now().year
    anios = {datos['anio'] for datos in alumnos.values()}
    edades = {anioActual - datos['anio'] for datos in alumnos.values()}

    print("Años:", sorted(anios))
    print("Edades:", sorted(edades))
    print("\nProducto cartesiano (año, edad):")
    for par in product(sorted(anios), sorted(edades)):
        print(par)
# Menú principal (comentado para evitar ejecución automática)
################## MENU #############################
opciones = {
    '1': lambda: menuUnion(conjuntosDniAlumnos),
    '2': lambda: menuInterseccion(conjuntosDniAlumnos),
    '3': lambda: menuDiferencia(conjuntosDniAlumnos),
    '4': lambda: menuDiferenciaSimetrica(conjuntosDniAlumnos),
    '5': lambda: menuFrecuencia(ALUMNOS),
    '6': lambda: menuSumaDigitos(ALUMNOS),
    '7': lambda: menuDigitoCompartido(conjuntosDniAlumnos),
    '8': lambda: menuDiversidadAlta(conjuntosDniAlumnos),
    '9': lambda: menuSumaTotalDigitosDni(ALUMNOS),
    '10': lambda: menuCompatibilidadDnis(conjuntosDniAlumnos),
    '11': lambda: menuCantAniosParesImpares(ANIOS),
    '12': lambda: menuGrupoZoBoomers(ANIOS),
    '13': lambda: menuVerificaBisiesto(ANIOS),
    '14': lambda: menuProdCartesianoAniosEdades(ALUMNOS)
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
