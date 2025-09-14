# Definimos la función
def calcular_promedio_por_ciudad(ciudades, temperaturas):
    resultados = {}

    for i, ciudad in enumerate(temperaturas):  # Iterar sobre ciudades
        suma_total = 0
        conteo = 0
        for semana in ciudad:  # Iterar sobre semanas
            for dia in semana:  # Iterar sobre días
                suma_total += dia["temp"]
                conteo += 1
        promedio = suma_total / conteo
        resultados[ciudades[i]] = promedio

    return resultados


# DATOS DE EJEMPLO (3 ciudades, 4 semanas, 7 días)

ciudades = ["Quito", "Guayaquil", "Cuenca"]

temperaturas = [
    [  # Quito
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 20}, {"day": "Miércoles", "temp": 19},
         {"day": "Jueves", "temp": 21}, {"day": "Viernes", "temp": 22}, {"day": "Sábado", "temp": 20},
         {"day": "Domingo", "temp": 19}],
        [{"day": "Lunes", "temp": 19}, {"day": "Martes", "temp": 21}, {"day": "Miércoles", "temp": 20},
         {"day": "Jueves", "temp": 22}, {"day": "Viernes", "temp": 23}, {"day": "Sábado", "temp": 21},
         {"day": "Domingo", "temp": 20}],
        [{"day": "Lunes", "temp": 20}, {"day": "Martes", "temp": 22}, {"day": "Miércoles", "temp": 21},
         {"day": "Jueves", "temp": 23}, {"day": "Viernes", "temp": 24}, {"day": "Sábado", "temp": 22},
         {"day": "Domingo", "temp": 21}],
        [{"day": "Lunes", "temp": 21}, {"day": "Martes", "temp": 23}, {"day": "Miércoles", "temp": 22},
         {"day": "Jueves", "temp": 24}, {"day": "Viernes", "temp": 25}, {"day": "Sábado", "temp": 23},
         {"day": "Domingo", "temp": 22}]
    ],
    [  # Guayaquil
        [{"day": "Lunes", "temp": 28}, {"day": "Martes", "temp": 30}, {"day": "Miércoles", "temp": 29},
         {"day": "Jueves", "temp": 31}, {"day": "Viernes", "temp": 32}, {"day": "Sábado", "temp": 30},
         {"day": "Domingo", "temp": 29}],
        [{"day": "Lunes", "temp": 29}, {"day": "Martes", "temp": 31}, {"day": "Miércoles", "temp": 30},
         {"day": "Jueves", "temp": 32}, {"day": "Viernes", "temp": 33}, {"day": "Sábado", "temp": 31},
         {"day": "Domingo", "temp": 30}],
        [{"day": "Lunes", "temp": 30}, {"day": "Martes", "temp": 32}, {"day": "Miércoles", "temp": 31},
         {"day": "Jueves", "temp": 33}, {"day": "Viernes", "temp": 34}, {"day": "Sábado", "temp": 32},
         {"day": "Domingo", "temp": 31}],
        [{"day": "Lunes", "temp": 31}, {"day": "Martes", "temp": 33}, {"day": "Miércoles", "temp": 32},
         {"day": "Jueves", "temp": 34}, {"day": "Viernes", "temp": 35}, {"day": "Sábado", "temp": 33},
         {"day": "Domingo", "temp": 32}]
    ],
    [  # Cuenca
        [{"day": "Lunes", "temp": 15}, {"day": "Martes", "temp": 16}, {"day": "Miércoles", "temp": 15},
         {"day": "Jueves", "temp": 17}, {"day": "Viernes", "temp": 18}, {"day": "Sábado", "temp": 16},
         {"day": "Domingo", "temp": 15}],
        [{"day": "Lunes", "temp": 16}, {"day": "Martes", "temp": 17}, {"day": "Miércoles", "temp": 16},
         {"day": "Jueves", "temp": 18}, {"day": "Viernes", "temp": 19}, {"day": "Sábado", "temp": 17},
         {"day": "Domingo", "temp": 16}],
        [{"day": "Lunes", "temp": 17}, {"day": "Martes", "temp": 18}, {"day": "Miércoles", "temp": 17},
         {"day": "Jueves", "temp": 19}, {"day": "Viernes", "temp": 20}, {"day": "Sábado", "temp": 18},
         {"day": "Domingo", "temp": 17}],
        [{"day": "Lunes", "temp": 18}, {"day": "Martes", "temp": 19}, {"day": "Miércoles", "temp": 18},
         {"day": "Jueves", "temp": 20}, {"day": "Viernes", "temp": 21}, {"day": "Sábado", "temp": 19},
         {"day": "Domingo", "temp": 18}]
    ]
]

# Uso de la función
resultados = calcular_promedio_por_ciudad(ciudades, temperaturas)

# Mostrar resultados
print("Temperaturas promedio por ciudad:\n")
for ciudad, promedio in resultados.items():
    print(f"{ciudad}: {promedio:.2f} °C")
    #