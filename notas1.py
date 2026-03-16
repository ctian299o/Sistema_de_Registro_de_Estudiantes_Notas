estudiantes = {}

def registrar_estudiante():
    print("\n── REGISTRAR ESTUDIANTE ──")
    id_est = input("ID / Código : ").strip()
    if id_est in estudiantes:
        print("⚠  Ese ID ya existe.")
        return
    nombre = input("Nombre      : ").strip()
    if not nombre:
        print("⚠  El nombre no puede estar vacío.")
        return
    estudiantes[id_est] = {"nombre": nombre, "materias": []}
    print(f"✓  {nombre} registrado correctamente.")