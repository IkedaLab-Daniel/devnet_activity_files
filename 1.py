import simplecal

addResult = simplecal.add(1,6)
subtractResult = simplecal.substract(5, 2)
multiplyResult = simplecal.multiply(10, 5)
divideResult = simplecal.divide(100, 10)
moduleResult = simplecal.modulo(3, 2)

print("Add: (1,6): ", addResult)
print("Substract: (5,2): ", subtractResult)
print("Multiply: (10,5): ", multiplyResult)
print("Divide: (100,10): ", divideResult)
print("Modulo: (3,2): ", moduleResult)

simplecal.loop_prompt()

if __name__ == "__main__":
    print("THIS IS PRINT ON MAIN")