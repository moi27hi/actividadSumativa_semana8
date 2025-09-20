import sys 
from  PyQt5.QtWidgets import (QApplication,QWidget,QVBoxLayout,QPushButton,QLineEdit,QLabel,QMessageBox)

def desarrollar_conversion(operacion):
    try:
       num1 = float(entrada1.text())
        
       if operacion == "kg_a_lbs":
              resultado = num1 * 2.20462
              QMessageBox.information(ventana, "Resultado", f"El resultado es: {round(resultado,2)} libras")
       elif operacion == "lbs_a_kg":
                resultado = num1 / 2.20462
                QMessageBox.information(ventana, "Resultado", f"El resultado es: {round(resultado,2)} kilogramos")
       elif operacion == "pies_a_metros":
                resultado = num1 / 3.28084
                QMessageBox.information(ventana, "Resultado", f"El resultado es: {round(resultado,2)} metros")
       elif operacion == "metros_a_pies":
                resultado = num1 * 3.28084
                QMessageBox.information(ventana, "Resultado", f"El resultado es: {round(resultado,2)} pies")
    except ValueError:
        QMessageBox.warning(ventana, "Error", "Por favor, ingrese un número válido.")

        # Creacion de la aplicación 
app = QApplication(sys.argv)




# Creacion de la ventana
ventana = QWidget()
ventana.setWindowTitle("Convertidor de Peso y Estatura") # Titulo de la ventana
ventana.resize(300,250) # Tamaño de la ventana
ventana.show() # Mostrar la ventana

# Creacion de los elementos de la ventana

label1 = QLabel("Ingrese el valor a convertir:")
entrada1 = QLineEdit()
boton_kg_a_lbs = QPushButton("Convertir kg a lbs")
boton_lbs_a_kg = QPushButton("Convertir lbs a kg")
boton_pies_a_metros = QPushButton("Convertir pies a metros")
boton_metros_a_pies = QPushButton("Convertir metros a pies")

# Conexión de los botones a las funciones
boton_kg_a_lbs.clicked.connect(lambda: desarrollar_conversion("kg_a_lbs"))
boton_lbs_a_kg.clicked.connect(lambda: desarrollar_conversion("lbs_a_kg")) 
boton_pies_a_metros.clicked.connect(lambda: desarrollar_conversion("pies_a_metros"))
boton_metros_a_pies.clicked.connect(lambda: desarrollar_conversion("metros_a_pies"))

# Agregar widgets al layout
layout = QVBoxLayout()
layout.addWidget(label1)
layout.addWidget(entrada1)
layout.addWidget(boton_kg_a_lbs)
layout.addWidget(boton_lbs_a_kg)
layout.addWidget(boton_pies_a_metros)
layout.addWidget(boton_metros_a_pies)

# Establecer el layout en la ventana
ventana.setLayout(layout)


# iniciar la aplicación
sys.exit(app.exec_())