from modelo.libro import Libro
from modelo.estudiante import Estudiante
from modelo.biblioteca import Biblioteca
from faker import Faker
import random

""""
    Sistema de gestión de biblioteca UNEMI
    
"""

# El punto de entrada del programa, donde se simulan las operaciones de la biblioteca
def main():
    fake = Faker('es_ES')
    
    # --- Crear la biblioteca ---
    print("=" * 60)
    print("  SISTEMA DE GESTIÓN DE BIBLIOTECA UNEMI")
    print("=" * 60)

    biblioteca = Biblioteca("Biblioteca Central UNEMI")
    print(f"\n{biblioteca}\n")

    # --- Registrar libros (RF-01) ---
    print("-- Registrando libros --")
    libros = []
    for _ in range(10):
        isbn = fake.unique.isbn13()
        titulo = fake.catch_phrase()
        autor = fake.name()
        libro = Libro(isbn, titulo, autor)
        libros.append(libro)
        biblioteca.registrar_libro(libro)

    # --- Registrar estudiantes (RF-02) ---
    print("\n-- Registrando estudiantes --")
    estudiantes = []
    carreras = ["Ingeniería en Sistemas", "Ingeniería Industrial", "Medicina", "Derecho", "Psicología"]
    for _ in range(5):
        # Utilizando el estilo de numerify para generar una cédula válida
        cedula = fake.unique.numerify(text="##########")
        nombre = fake.first_name()
        apellido = fake.last_name()
        carrera = random.choice(carreras)
        est = Estudiante(cedula, nombre, apellido, carrera)
        estudiantes.append(est)
        biblioteca.registrar_estudiante(est)

    # --- Estado actual ---
    print(f"\n{biblioteca}\n")

    # --- Realizar préstamos (RF-03 y RF-04) ---
    print("-- Realizando 15 intentos de préstamos --")
    # Para tener 10 exitosos y 5 fallidos, intentaremos prestar 
    # los 10 primeros libros de forma normal, y luego intentaremos 
    # volver a prestar 5 de esos libros que ya están prestados.
    intentos_indices_libros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4]
    
    for i, idx_libro in enumerate(intentos_indices_libros):
        libro = libros[idx_libro]
        # Distribuimos los préstamos entre los 5 estudiantes
        estudiante = estudiantes[i % 5]
        
        fecha_prestamo = "2026-04-15"
        fecha_devolucion = "2026-04-30"
        
        print(f"\nIntento {i+1}: Prestando '{libro.titulo}' a {estudiante.nombre}")
        resultado = biblioteca.prestar_libro(
            libro.isbn, estudiante.cedula, fecha_prestamo, fecha_devolucion
        )
        print(resultado)


    # --- Consultar préstamos activos (RF-06) ---
    print(f"\n-- Préstamos activos de {estudiantes[0].nombre} {estudiantes[0].apellido} --")
    prestamos_est0 = biblioteca.consultar_prestamos_activos(estudiantes[0].cedula)
    if prestamos_est0:
        for prestamo in prestamos_est0:
            print(f"  -> {prestamo}")
    else:
        print("  (Sin préstamos activos)")

    # --- Devolver un libro (RF-05) ---
    print("\n-- Devolviendo un libro --")
    # Devolvemos el primer libro que fue prestado al estudiante 0
    if prestamos_est0:
        libro_a_devolver = prestamos_est0[0].libro
        resultado = biblioteca.devolver_libro(libro_a_devolver.isbn, estudiantes[0].cedula)
        print(resultado)

        # --- Verificar que el libro está disponible nuevamente ---
        print(f"\n-- Estado del libro devuelto --")
        print(f"  {libro_a_devolver}")

    # --- Estado final ---
    print(f"\n{'=' * 60}")
    print(f"  {biblioteca}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    main()