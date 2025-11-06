# -*- coding: utf-8 -*-

#Agregar un atributo al objeto Alumno de Edad. Si es mayor de edad que imprima un mensaje
import sys
from pathlib import Path
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
)

class Alumno:
    """Clase que representa un alumno."""

    def __init__(self, nombre, carrera, edad):
        self.nombre = nombre
        self.carrera = carrera
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18


class RegistroAlumnos(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de Alumnos")
        self.resize(350, 180)

        # ------------------ Widgets ------------------
        self.nombre_edit = QLineEdit(self)
        self.nombre_edit.setPlaceholderText("Ej.: Ana García")

        self.carrera_edit = QLineEdit(self)
        self.carrera_edit.setPlaceholderText("Ej.: Ingeniería Informática")

        self.edad_edit = QLineEdit(self)
        self.edad_edit.setPlaceholderText("Ej.: 42")

        self.guardar_btn = QPushButton("Guardar", self)
        self.guardar_btn.clicked.connect(self.guardar_alumno)

        # Botón Limpiar (opcional)
        self.limpiar_btn = QPushButton("Limpiar", self)
        self.limpiar_btn.clicked.connect(self.limpiar_campos)

        # ------------------ Layout -------------------
        form_layout = QVBoxLayout()

        # Nombre
        fila_nombre = QHBoxLayout()
        fila_nombre.addWidget(QLabel("Nombre:", self))
        fila_nombre.addWidget(self.nombre_edit)
        form_layout.addLayout(fila_nombre)

        # Carrera
        fila_carrera = QHBoxLayout()
        fila_carrera.addWidget(QLabel("Carrera:", self))
        fila_carrera.addWidget(self.carrera_edit)
        form_layout.addLayout(fila_carrera)

        # Edad
        fila_edad = QHBoxLayout()
        fila_edad.addWidget(QLabel("Edad:", self))
        fila_edad.addWidget(self.edad_edit)
        form_layout.addLayout(fila_edad)

        # Botones
        botones_layout = QHBoxLayout()
        botones_layout.addStretch()
        botones_layout.addWidget(self.guardar_btn)
        botones_layout.addWidget(self.limpiar_btn)
        form_layout.addLayout(botones_layout)

        self.setLayout(form_layout)

        # Ruta del archivo donde se guardarán los datos
        self.ruta_archivo = Path("alumnos.txt")

    # -------------------------------------------------
    def guardar_alumno(self):
        nombre = self.nombre_edit.text().strip()
        carrera = self.carrera_edit.text().strip()
        edad_texto = self.edad_edit.text().strip()

        if not nombre or not carrera or not edad_texto:
            QMessageBox.warning(
                self,
                "Campos incompletos",
                "Debes rellenar tanto el nombre como la carrera.",
            )
            return

        try:
            edad = int(edad_texto)
        except ValueError:
            QMessageBox.warning(
                self,
                "Edad inválida",
                "La edad debe ser un número entero.",
            )
            return

        alumno = Alumno(nombre, carrera, edad)

        linea = f"{alumno.nombre} – {alumno.carrera} – Edad: {alumno.edad}\n"

        try:
            with self.ruta_archivo.open("a", encoding="utf-8") as f:
                f.write(linea)
        except OSError as e:
            QMessageBox.critical(
                self,
                "Error de escritura",
                f"No se pudo guardar el registro.\nDetalle: {e}",
            )
            return

        mensaje = f"Alumno guardado correctamente en '{self.ruta_archivo}'."
        if alumno.es_mayor_de_edad():
            mensaje += "\n El alumno es mayor de edad."

        QMessageBox.information(self, "Guardado", mensaje)
        self.limpiar_campos()

    def limpiar_campos(self):
        self.nombre_edit.clear()
        self.carrera_edit.clear()
        self.edad_edit.clear()
        self.nombre_edit.setFocus()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = RegistroAlumnos()
    ventana.show()
    sys.exit(app.exec_())