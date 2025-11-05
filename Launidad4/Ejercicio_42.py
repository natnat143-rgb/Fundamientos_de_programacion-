# -*- coding: utf-8 -*-
"""

Requisitos:
"""

#Comentar cuales son las librerias que se importan y para que funciona cada una 

#

import sys  #Proporciona acceso a funciones y variables del sistema, como argumentos de línea de comandos y salida del programa.
import platform  #Permite identificar el sistema operativo en el que se ejecuta el programa (Windows, Linux, macOS, etc.).
import subprocess  #Permite ejecutar comandos del sistema operativo desde Python y capturar su salida.

from PyQt5.QtWidgets import (  # Importa los componentes gráficos necesarios para construir la interfaz de usuario.

    QApplication,  # Clase principal que gestiona la aplicación Qt.

    QWidget,       # Clase base para todos los objetos de interfaz gráfica.

    QLabel,        # Etiqueta de texto estático.

    QLineEdit,     # Campo de texto para entrada de usuario.

    QPushButton,   # Botón interactivo.

    QTextEdit,     # Área de texto multilínea para mostrar resultados.

    QVBoxLayout,   # Layout vertical para organizar widgets en columna.

    QHBoxLayout,   # Layout horizontal para organizar widgets en fila.
    
    QMessageBox,   # Cuadro de diálogo para mostrar mensajes al usuario.
)


class PingApp(QWidget):
    """Ventana principal de la aplicación."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ping – PyQt5")
        self.resize(400, 300)

        # ---------- Widgets ----------
        # Entrada de host / IP
        self.host_input = QLineEdit(self)
        self.host_input.setPlaceholderText("Ejemplo: google.com o 8.8.8.8")

        # Botón de ejecutar ping
        self.ping_btn = QPushButton("Enviar ping", self)
        self.ping_btn.clicked.connect(self.ejecutar_ping)

        # Área de texto donde se mostrará la salida
        self.resultado = QTextEdit(self)
        self.resultado.setReadOnly(True)

        # ---------- Layout ----------
        entrada_layout = QHBoxLayout()
        entrada_layout.addWidget(QLabel("Destino:", self))
        entrada_layout.addWidget(self.host_input)

        main_layout = QVBoxLayout()
        main_layout.addLayout(entrada_layout)
        main_layout.addWidget(self.ping_btn)
        main_layout.addWidget(QLabel("Resultado:", self))
        main_layout.addWidget(self.resultado)

        self.setLayout(main_layout)

    # -----------------------------------------------------------------
    def ejecutar_ping(self):
        """Construye y ejecuta el comando ping, mostrando la salida."""
        host = self.host_input.text().strip()
        if not host:
            QMessageBox.warning(self, "Entrada vacía", "Introduce una dirección IP o nombre de host.")
            return

        # Determinar parámetros según SO
        sistema = platform.system().lower()
        if "windows" in sistema:
            cmd = ["ping", "-n", "4", host]         
        else:  # Linux, macOS, etc.
            cmd = ["ping", "-c", "4", host]       

        try:
            # Ejecutamos el comando y capturamos stdout + stderr
            proceso = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=10,            
            )
            salida = proceso.stdout if proceso.returncode == 0 else proceso.stderr
            self.resultado.setPlainText(salida)
        except subprocess.TimeoutExpired:
            self.resultado.setPlainText("Error: tiempo de espera agotado.")
        except Exception as e:
            self.resultado.setPlainText(f"Ocurrió un error inesperado:\n{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PingApp()
    ventana.show()
    sys.exit(app.exec_())