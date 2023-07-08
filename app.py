from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "systemshop"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        matricula = request.form['matricula']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM registro WHERE Matricula = %s AND correo = %s"
        values = (matricula, correo)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            stored_password = user[5]
            if contrasena == stored_password:
                return redirect(url_for('producto_servicio'))
            else:
                flash('Contraseña incorrecta')
        else:
            flash('Datos de inicio de sesión incorrectos')

        cursor.close()

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

        cursor = mysql.connection.cursor()
        query = "INSERT INTO registro (Matricula, correo, grupo, nombre, apellido_paterno, contrasena) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (matricula, correo, grupo, nombre, apellido_paterno, contrasena)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        flash('Registro exitoso. ¡Ahora puedes iniciar sesión!')

    return redirect(url_for('menu'))

@app.route('/producto-servicio')
def producto_servicio():
    cursor = mysql.connection.cursor()
    query_servicios = "SELECT * FROM Servicios"
    cursor.execute(query_servicios)
    servicios = cursor.fetchall()

    query_productos = "SELECT * FROM Producto"
    cursor.execute(query_productos)
    productos = cursor.fetchall()

    cursor.close()

    return render_template('producto_servicio.html', servicios=servicios, productos=productos)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
