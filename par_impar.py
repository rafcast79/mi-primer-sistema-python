while True:
    try:
        numero = int(input("Hakuna matata: "))
        if numero < 0:
            print("El numero digitado es negativo")
        elif numero == 0:
            print("El numero es cero")
        elif numero > 100:
            print("El numero es muuy grande para detectarlo")
        else:
            if numero % 2 == 0:
                print("Es par")
            else:
                print("Es impar")
    except:
        print("Eso es un texto 😂")