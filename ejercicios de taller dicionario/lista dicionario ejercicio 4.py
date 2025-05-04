estudiantes = {"1": {"nombre": "Lorea", "nota": 8}}
for i in range(2, 11):
    n = input("Nombre: ")
    nota = float(input("Nota: "))
    estudiantes[str(i)] = {"nombre": n, "nota": nota}

print("\nestudiantes = {")
for k, v in estudiantes.items():
    print(f'  "{k}": {{"nombre": "{v["nombre"]}", "nota": {v["nota"]}}},')
print("}")

a = [v["nombre"] for v in estudiantes.values() if v["nota"] >= 5]
s = [v["nombre"] for v in estudiantes.values() if v["nota"] < 5]
m = sum(v["nota"] for v in estudiantes.values()) / len(estudiantes)

print("\nAprobados:", a)
print("Suspendidos:", s)
print("Media:", round(m, 2))