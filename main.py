from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,QFontDialog,QTimeEdit, QLineEdit, QTextEdit)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont 
# Agregar el resto de componentes segun requiera

# CONSTANTES (parametros de inicializacion)
ANCHO, ALTO = 800, 500
TITULO = 'Agenda Creativa - Organizador de proyectos' 
text_btn = 'Enviar'
text_input = 'Ingrease algo...'

# CLASE PRINCIPAL (VENTANA)
class MainWindow(QWidget):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
           
        self.materiales = []
        self.insumos = {}
        self.bocetos = []
        self.proyectos = []
        self.temporizador_activo = False
        self.tiempo_restante = 0

        self.set_window()
        self.config_window()
        self.event_handler()
        self.show()

    def set_window(self):
        self.btn = QPushButton(text_btn)
        self.btn.setStyleSheet(''' 
                              color: #ffffff;
                              background-color: ##6434eb;
                              border-radius: 15px;
                              padding: 10px;
                              font - weigth: 600;
        
        ''')
        self.texto = QLabel()
        self.texto_temporizador = QLabel (self)
        self.texto.setFont()
        self.input = QLineEdit(text_input)
        self.timer = Qtimer (self)
        self.timer.setInterval (1000)
        

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.input, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.btn, alignment=Qt.AlignLeft)
        self.main_layout.addWidget(self.texto, alignment=Qt.AlignCenter)

        self.setLayout(self.main_layout)

    def config_window(self):
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)
        font = QFont ('Arial', 14, QFont.Cursive, True)
        self.setFont (font)

        # Adaptar segun requie

    def event_handler(self):
        # GESTION Y MANEJO DE EVENTOS (INTERACCION DEK USUARIO)
        self.btn.clicked.connect(self.set_text)
        self.timer.timeout.connect(self.actualizar_temporizador)
        

    def set_text(self):
        cadena = self.input.text()
        self.texto.setText(cadena)

    def actualizar_temporizador(self):

        #logica que reste el tiempo 
        self.texto_temporizador.setText(str(self.tiempo_restante))



# FUNCION PARA EJECUTAR LA APP
def run():
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()


