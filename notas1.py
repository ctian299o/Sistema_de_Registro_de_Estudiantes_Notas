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

def registrar_materia():
    print("\n── REGISTRAR MATERIA Y NOTA ──")
    if not estudiantes:
        print("⚠  No hay estudiantes registrados.")
        return
    listar_estudiantes(resumen=True)
    id_est = input("ID del estudiante : ").strip()
    if id_est not in estudiantes:
        print("⚠  ID no encontrado.")
        return
    materia = input("Materia           : ").strip()
    if not materia:
        print("⚠  La materia no puede estar vacía.")
        return
    try:
        nota = float(input("Nota (0–10)       : "))
        if not (0 <= nota <= 10):
            raise ValueError
    except ValueError:
        print("⚠  Nota inválida. Debe ser un número entre 0 y 10.")
        return
    estudiantes[id_est]["materias"].append({"materia": materia, "nota": nota})
    print(f"✓  {materia} con nota {nota} agregada a {estudiantes[id_est]['nombre']}.")
