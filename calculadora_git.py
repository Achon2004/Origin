# Calculadora simple en Python
def sumar(a: float, b: float) -> float:
    return a + b

def restar(a: float, b: float) -> float:
    return a - b

def multiplicar(a: float, b: float) -> float:
    return a * b

def dividir(a: float, b: float) -> float:
    if b != 0:
        return a / b
    raise ValueError("Error: División por cero no permitida.")

def potencia(a: float, b: float) -> float:
    return a ** b

def elevar_cubo(a: float) -> float:
    return a ** 3

if __name__ == "__main__":
    print(sumar(2,3))
    print(restar(5,1))
    print(multiplicar(4,2))
    print(dividir(10,2))
    print(potencia(2,3))
    print(elevar_cubo(5))