print("Bienvenido a la mejor calculadora")
print("Para salir solo escribe salir")
print("las operaciones son: suma, resta, multiplicacion y division")

resultado = 0
while True:
    if resultado == 0:
        resultado = int(input("ingrese numero: "))
        if resultado == "salir":
            break
    op = input("ingresa operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multiplicacion":
        resultado *= n2
    elif op.lower() == "division":
        if n2 != 0:
            resultado /= n2
        else:
            print("No se puede dividir entre cero.")
            break
    else:
        print("operacion no valida")
        break

    print(f"el resultado es {resultado}")

print("Gracias por utilizar la calculadora.")
