
Operation = input("Enter operation: ")

# Dividir la entrada en componentes
try:
    x, y, z = Operation.split()
    x = float(x)
    z = float(z)
except ValueError:
    print("Invalid format")
    exit()

# Realizar la operación
if y == "+":
    resultado = x + z
elif y == "-":
    resultado = x - z
elif y == "*":
    resultado = x * z
elif y == "/":
    if z == 0:
        print("Error: Division by zero.")
        exit()
    resultado = x / z
else:
    print("Invalid operation. Use '+', '-', '*', or '/'.")
    exit()


print(f"{resultado:.1f}")

