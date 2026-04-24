notas = {"Derecho": 90, "Sistemas": 95, "Inglés": 60}
aprobados = {k: v for k, v in notas.items() if v >= 70}
print(f"Materias aprobadas: {aprobados}")