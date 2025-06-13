def agregar_notas(lista):
    try:
        nota = 0
        while nota <= 0:
            nota = float(input("Ingrese nota:\n"))
        lista.append(nota)
        print("La nota fue agregada con éxito!")
    except:
        print("La nota debe ser un valor numerico decimal o entero")