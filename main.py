from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
from faker import Faker

fake = Faker("es_ES")


def main():

    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")

# ─── Generar libros ───
    print("── Registrando libros ──")
    libros = []

    for _ in range(3):
        libro = Libro(
            str(fake.isbn13()),
            fake.sentence(nb_words=3),
            fake.name(),
        )
        libros.append(libro)
        biblioteca.registrar_libro(libro)

# ─── Generar estudiantes ───
    print("\n── Registrando estudiantes ──")
    estudiantes = []

    for _ in range(3):
        est = Estudiante(
            str(fake.random_number(digits=9, fix_len=True)), 
            fake.first_name(),
            fake.last_name(),
            fake.job()
        )
        estudiantes.append(est)
        biblioteca.registrar_estudiante(est)

    print(f"\n{biblioteca}\n")

# ─── Préstamos ───
    print("\n── Realizando préstamos ──")

    for i in range(3):
        resultado = biblioteca.prestar_libro(
            libros[i].isbn,
            estudiantes[i].cedula,
            fake.date(),
            fake.date()
        )
        print(resultado)

# ─── Intentar prestar libro ya prestado ───
    print("\n── Intentando prestar libro ya prestado ──")

    resultado = biblioteca.prestar_libro(
        libros[0].isbn,
        estudiantes[1].cedula,
        fake.date(),
        fake.date()
    )
    print(resultado)

# ─── Consultar préstamos ───
    print(f"\n── Préstacmos activos de {estudiantes[0].nombre} ──")

    prestamos_est = biblioteca.consultar_prestamos_activos(estudiantes[0].cedula)

    for prestamo in prestamos_est:
        print(f"  → {prestamo}")

# ─── Devolver ───
    print("\n── Devolviendo un libro ──")

    resultado = biblioteca.devolver_libro(
        libros[0].isbn,
        estudiantes[0].cedula
    )
    print(resultado)

# ─── Estado del libro ───
    print(f"\n── Estado del libro devuelto ──")
    print(f"  {libros[0]}")

# ─── Consultar después ───
    print(f"\n── Préstamos activos de {estudiantes[0].nombre} (después de devolución) ──")

    prestamos_est = biblioteca.consultar_prestamos_activos(estudiantes[0].cedula)

    if prestamos_est:
        for prestamo in prestamos_est:
            print(f"  → {prestamo}")
    else:
        print("  (Sin préstamos activos)")

# ─── Prestar otra vez ───
    print("\n── Prestando el libro devuelto a otro estudiante ──")

    resultado = biblioteca.prestar_libro(
        libros[0].isbn,
        estudiantes[1].cedula,
        fake.date(),
        fake.date()
    )
    print(resultado)

# ─── Estado final ───
    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()