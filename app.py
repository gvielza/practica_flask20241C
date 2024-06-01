from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resultados')
def resultados():
    dni = request.args.get('dni')
    usuario = request.args.get('usuario')
    return render_template('resultados.html', dni=dni, usuario=usuario)