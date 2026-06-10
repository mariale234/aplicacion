from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QTabWidget, 
QListWidget, QColorDialog, QSpinBox, QDateEdit, QGroupBox, QGridLayout, QMessageBox)
from PyQt5.QtCore import Qt, QTimer, QDate
from PyQt5.QtGui import QFont, QColor

# CONSTANTES 
ANCHO, ALTO = 900, 600
TITULO = 'Agenda Creativa - Organizador de proyectos' 

# CLASE PRINCIPAL 
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
        # Pestañas principales
        self.tabs = QTabWidget()
        self.tab_diseno = QWidget()
        self.tab_control = QWidget()
        self.tab_proyectos = QWidget()
        
        self.tabs.addTab(self.tab_diseno, "DISEÑO")
        self.tabs.addTab(self.tab_control, "CONTROL")
        self.tabs.addTab(self.tab_proyectos, "PROYECTOS")
        
        # PESTAÑA DISEÑO 
        layout_diseno = QHBoxLayout()
        
        # Bocetos
        grupo_bocetos = QGroupBox("Bocetos")
        layout_bocetos = QVBoxLayout()
        self.bocetos_input = QTextEdit()
        self.bocetos_input.setPlaceholderText("Escribe tu idea...")
        self.bocetos_lista = QListWidget()
        self.btn_boceto = QPushButton("Guardar Boceto")
        layout_bocetos.addWidget(self.bocetos_input)
        layout_bocetos.addWidget(self.btn_boceto)
        layout_bocetos.addWidget(self.bocetos_lista)
        grupo_bocetos.setLayout(layout_bocetos)
        
        # Paleta de colores 
        grupo_paleta = QGroupBox("Paleta de Colores")
        layout_paleta = QVBoxLayout()
        
        # ingresar código HEX
        self.color_hex_input = QLineEdit()
        self.color_hex_input.setPlaceholderText("Ejemplo: #FF5733")
        
    
        self.color_label = QLabel("Color actual")
        self.color_label.setStyleSheet("background-color: white; min-height: 50px;")
        self.color_label.setAlignment(Qt.AlignCenter)
        

        self.btn_aplicar_color = QPushButton("Aplicar Color HEX")
        

        self.btn_guardar_color = QPushButton("Guardar Color")
        
        # Lista de colores guardados
        self.lista_colores = QListWidget()
        
        layout_paleta.addWidget(QLabel("Código HEX:"))
        layout_paleta.addWidget(self.color_hex_input)
        layout_paleta.addWidget(self.btn_aplicar_color)
        layout_paleta.addWidget(self.color_label)
        layout_paleta.addWidget(self.btn_guardar_color)
        layout_paleta.addWidget(QLabel("Colores guardados:"))
        layout_paleta.addWidget(self.lista_colores)
        
        grupo_paleta.setLayout(layout_paleta)
        
        layout_diseno.addWidget(grupo_bocetos)
        layout_diseno.addWidget(grupo_paleta)
        self.tab_diseno.setLayout(layout_diseno)
        
        # PESTAÑA CONTROl
        layout_control = QHBoxLayout()
        
        # Materiales
        grupo_materiales = QGroupBox("Materiales")
        layout_materiales = QVBoxLayout()
        self.material_input = QLineEdit()
        self.material_input.setPlaceholderText("Material...")
        self.materiales_lista = QListWidget()
        self.btn_material = QPushButton("Agregar Material")
        self.btn_eliminar_material = QPushButton("Eliminar Material")
        layout_materiales.addWidget(self.material_input)
        layout_materiales.addWidget(self.btn_material)
        layout_materiales.addWidget(self.materiales_lista)
        layout_materiales.addWidget(self.btn_eliminar_material)
        grupo_materiales.setLayout(layout_materiales)
        
        # Insumos
        grupo_insumos = QGroupBox("Insumos")
        layout_insumos = QVBoxLayout()
        self.insumo_nombre = QLineEdit()
        self.insumo_nombre.setPlaceholderText("Insumo...")
        self.insumo_cantidad = QSpinBox()
        self.insumo_cantidad.setRange(0, 1000)
        self.insumos_lista = QListWidget()
        self.btn_insumo = QPushButton("Agregar Insumo")
        self.btn_eliminar_insumo = QPushButton("Eliminar Insumo")
        layout_insumos.addWidget(self.insumo_nombre)
        layout_insumos.addWidget(self.insumo_cantidad)
        layout_insumos.addWidget(self.btn_insumo)
        layout_insumos.addWidget(self.insumos_lista)
        layout_insumos.addWidget(self.btn_eliminar_insumo)
        grupo_insumos.setLayout(layout_insumos)
        
        layout_control.addWidget(grupo_materiales)
        layout_control.addWidget(grupo_insumos)
        self.tab_control.setLayout(layout_control)
        
        #  PESTAÑA PROYECTOS
        layout_proyectos = QVBoxLayout()
        
        # Plazos
        grupo_plazos = QGroupBox("Plazos")
        layout_plazos = QGridLayout()
        self.fecha_entrega = QDateEdit()
        self.fecha_entrega.setDate(QDate.currentDate())
        self.nombre_proyecto = QLineEdit()
        self.nombre_proyecto.setPlaceholderText("Nombre del proyecto...")
        self.plazos_lista = QListWidget()
        self.btn_plazo = QPushButton("Registrar Plazo")

        layout_plazos.addWidget(QLabel("Fecha:"), 0, 0)
        layout_plazos.addWidget(self.fecha_entrega, 0, 1)
        layout_plazos.addWidget(QLabel("Proyecto:"), 1, 0)
        layout_plazos.addWidget(self.nombre_proyecto, 1, 1)
        layout_plazos.addWidget(self.btn_plazo, 2, 0, 1, 2)
        layout_plazos.addWidget(self.plazos_lista, 3, 0, 1, 2)
        grupo_plazos.setLayout(layout_plazos)
        
        # Temporizador
        grupo_temp = QGroupBox("Temporizador")
        layout_temp = QVBoxLayout()
        self.tiempo_input = QSpinBox()
        self.tiempo_input.setRange(0, 3600)
        self.tiempo_input.setValue(60)
        self.texto_temporizador = QLabel("Tiempo: 00:00")
        self.texto_temporizador.setAlignment(Qt.AlignCenter)
        self.btn_iniciar = QPushButton("Iniciar")
        self.btn_detener = QPushButton("Detener")
        botones_temp = QHBoxLayout()

        botones_temp.addWidget(self.btn_iniciar)
        botones_temp.addWidget(self.btn_detener)
        layout_temp.addWidget(self.tiempo_input)
        layout_temp.addWidget(self.texto_temporizador)
        layout_temp.addLayout(botones_temp)
        grupo_temp.setLayout(layout_temp)
        
        layout_proyectos.addWidget(grupo_plazos)
        layout_proyectos.addWidget(grupo_temp)
        self.tab_proyectos.setLayout(layout_proyectos)
        
        # Layout principal
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)

    def config_window(self):   #CONFIGURACION 
        self.resize(ANCHO, ALTO)
        self.setWindowTitle(TITULO)
        font = QFont('Arial', 10)
        self.setFont(font)

    def event_handler(self):
        # Conexiones Diseño
        self.btn_boceto.clicked.connect(self.guardar_boceto)
        self.btn_aplicar_color.clicked.connect(self.aplicar_color_hex)
        self.btn_guardar_color.clicked.connect(self.guardar_color)
        
        # Conexiones Control
        self.btn_material.clicked.connect(self.agregar_material)
        self.btn_eliminar_material.clicked.connect(self.eliminar_material)
        self.btn_insumo.clicked.connect(self.agregar_insumo)
        self.btn_eliminar_insumo.clicked.connect(self.eliminar_insumo)
        
        # Conexiones Proyectos
        self.btn_plazo.clicked.connect(self.registrar_plazo)
        self.btn_iniciar.clicked.connect(self.iniciar_temporizador)
        self.btn_detener.clicked.connect(self.detener_temporizador)
        
        # Temporizador
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.actualizar_temporizador)

    # MÉTODOS DISEÑO 
    def guardar_boceto(self):
        texto = self.bocetos_input.toPlainText()
        if texto:
            self.bocetos.append(texto)
            self.bocetos_lista.addItem(texto[:50])
            self.bocetos_input.clear()
    
    def aplicar_color_hex(self):
        """Aplica un color a partir de código HEX"""
        hex_color = self.color_hex_input.text().strip()
        
        # Asegurar que comience con # si no lo tiene
        if hex_color and not hex_color.startswith('#'):
            hex_color = '#' + hex_color
        
        # Aplicar el color directamente
        self.color_label.setStyleSheet(f"background-color: {hex_color}; min-height: 50px;")
        self.color_label.setText(hex_color.upper())
        self.color_hex_input.clear()
    
    def guardar_color(self):
        color = self.color_label.text()
        if color and color != "Color actual":
            self.lista_colores.addItem(color)
    
    #  MÉTODOS CONTROL
    def agregar_material(self):
        material = self.material_input.text()
        if material:
            self.materiales.append(material)
            self.materiales_lista.addItem(material)
            self.material_input.clear()
    
    def eliminar_material(self):
        fila = self.materiales_lista.currentRow()
        if fila >= 0:
            self.materiales.pop(fila)
            self.materiales_lista.takeItem(fila)
    
    def agregar_insumo(self):
        nombre = self.insumo_nombre.text()
        if nombre:
            self.insumos[nombre] = self.insumo_cantidad.value()
            self.actualizar_insumos()
            self.insumo_nombre.clear()
            self.insumo_cantidad.setValue(0)
    
    def eliminar_insumo(self):
        fila = self.insumos_lista.currentRow()
        if fila >= 0:
            nombre = list(self.insumos.keys())[fila]
            del self.insumos[nombre]
            self.actualizar_insumos()
    
    def actualizar_insumos(self):
        self.insumos_lista.clear()
        for nombre, cantidad in self.insumos.items():
            self.insumos_lista.addItem(f"{nombre}: {cantidad}")
    
    # MÉTODOS PROYECTOS 
    def registrar_plazo(self):
        fecha = self.fecha_entrega.date().toString("dd/MM/yyyy")
        proyecto = self.nombre_proyecto.text()
        if proyecto:
            self.plazos_lista.addItem(f"{proyecto} - {fecha}")
            self.nombre_proyecto.clear()
    
    def iniciar_temporizador(self):
        if not self.temporizador_activo:
            self.tiempo_restante = self.tiempo_input.value()
            self.temporizador_activo = True
            self.timer.start()
    
    def detener_temporizador(self):
        self.temporizador_activo = False
        self.timer.stop()
    
    def actualizar_temporizador(self):
        # resta el tiempo 
        if self.temporizador_activo and self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            self.texto_temporizador.setText(f"Tiempo: {minutos:02d}:{segundos:02d}")
            
            if self.tiempo_restante == 0:
                self.detener_temporizador()
                QMessageBox.information(self, "Temporizador", "¡Tiempo completado!")

# EJECUTAR LA APP
def run():
    app = QApplication([])
    main_window = MainWindow()
    app.exec_()

if __name__ == "__main__":
    run()
