from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

app.secret_key = 'mysecretkey'

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        # Realiza aquí la validación de inicio de sesión
        # Si el inicio de sesión es exitoso, redirige a producto_servicio.html
        return redirect(url_for('producto_servicio'))
    return render_template('menu.html')

@app.route('/registro')
def registro():
    return render_template('registro.html')

@app.route('/formulario-registro', methods=['POST'])
def guardar():
    if request.method == 'POST':
        matricula = request.form['matricula']
        correo = request.form['correo']
        grupo = request.form['grupo']
        nombre = request.form['nombre']
        apellido_paterno = request.form['apellido-paterno']
        contrasena = request.form['contrasena']

        # Aquí puedes guardar los datos en la base de datos o hacer lo que desees

        flash('Registro exitoso. ¡Ahora puedes iniciar sesión!')

    return redirect(url_for('menu'))

@app.route('/producto-servicio')
def producto_servicio():
    return render_template('producto_servicio.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
