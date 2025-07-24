from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    experiencia = int(request.form['experiencia'])
    estudios = request.form['estudios'].lower()

    califica = True
    motivos = []

    if edad < 18 or edad > 45:
        califica = False
        motivos.append("Edad fuera del rango permitido (18-45 años).")

    if experiencia < 1:
        califica = False
        motivos.append("Experiencia insuficiente.")

    if estudios not in ["tecnico", "universidad"]:
        califica = False
        motivos.append("Nivel de estudios insuficiente.")

    return render_template('resultado.html', nombre=nombre, califica=califica, motivos=motivos)

if __name__ == '__main__':
    app.run(debug=True)
