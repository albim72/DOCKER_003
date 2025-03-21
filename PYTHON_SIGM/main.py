import numpy as np

def sigmoid(x):
    return 1/(1+np.exp(-x))

if __name__ == '__main__':
    x = float(input("Podaj wartość argumentu funckji sigmoid: "))
    print(f"wartość funckji sigmoid dla x = {x} wynosi {sigmoid(x):.6f}")
