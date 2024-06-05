from flask import Flask, render_template, request
from base_datos.conexion import Conexion

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados')
def resultados():
    dni = request.args.get('dni')
    usuario = request.args.get('usuario')
    contrasenna=request.args.get('password')
    conexion=Conexion('base_datos/usuarios.db')
    conexion.crear_tabla_cliente()
    conexion.agregar_cliente(dni,usuario,contrasenna)
    clientes=conexion.mostrar_clientes()
    conexion.cerrar_conexion()
    mensaje="Se guardo exitosamente en la base de datos"
    return render_template('resultados.html', dni=dni, usuario=usuario, mensaje=mensaje,clientes=clientes)