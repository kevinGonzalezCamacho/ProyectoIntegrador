# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.static_folder = 'static'

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "systemshop"

app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('menu'))

@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM dbo_estudiantes WHERE Correo = %s"
        values = (correo,)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            stored_password = user[7]
            if contrasena == stored_password:
                return redirect(url_for('Inicio'))
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

@app.route('/misPublicaciones')
def mostrar_publicaciones():
    # Conecta a la base de datos
    cursor = mysql.connection.cursor()

    # Consulta para obtener las publicaciones desde la tabla "productos"
    query = "SELECT * FROM dbo_producto"
    cursor.execute(query)
    dbo_producto = cursor.fetchall()

    print(dbo_producto)
    # Cierra la conexión a la base de datos
    cursor.close()

    return render_template('misPublicaciones.html', publicaciones=dbo_producto)

@app.route('/producto-servicio')
def producto_servicio():
    cursor = mysql.connection.cursor()
    query_servicios = "SELECT * FROM dbo_servicios"
    cursor.execute(query_servicios)
    servicios = cursor.fetchall()

    query_productos = "SELECT * FROM dbo_producto"
    cursor.execute(query_productos)
    productos = cursor.fetchall()

    cursor.close()

    return render_template('producto_servicio.html', servicios=servicios, productos=productos)

@app.route('/eliminar-servicio/<int:servicio_id>', methods=['DELETE'])
def eliminar_servicio(servicio_id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM Servicios WHERE id_servicio = %s"
    values = (servicio_id,)
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()

    return '', 204

@app.route('/eliminar-producto/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM Producto WHERE id_producto = %s"
    values = (producto_id,)
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()

    return '', 204

@app.route('/buscar-producto', methods=['GET'])
def buscar_producto():
    if request.method == 'GET':
        product_name = request.args.get('product_name')

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM dbo_producto WHERE nombre LIKE %s"
        values = ('%' + product_name + '%',)
        cursor.execute(query, values)
        productos = cursor.fetchall()
        cursor.close()

        return render_template('producto_servicio.html', servicios=[], productos=productos)

@app.route('/buscar-servicio', methods=['GET'])
def buscar_servicio():
    if request.method == 'GET':
        service_name = request.args.get('service_name')
        if service_name is None:
            service_name = ""

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM dbo_servicios WHERE nombre LIKE %s"
        values = ('%' + service_name + '%',)
        cursor.execute(query, values)
        servicios = cursor.fetchall()
        cursor.close()

        return render_template('producto_servicio.html', servicios=servicios, productos=[])

@app.route('/agregar-servicio')
def agregar_servicio():
    return render_template('agregar_servicio.html')

@app.route('/guardar-servicio', methods=['POST'])
def guardar_servicio():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        start_date = request.form['start_date']
        end_date = request.form['end_date']

        cursor = mysql.connection.cursor()
        query = "INSERT INTO Servicios (nombre, precio, fecha_inicio, fecha_fin) VALUES (%s, %s, %s, %s)"
        values = (name, price, start_date, end_date)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        flash('Servicio agregado correctamente')

    return redirect(url_for('producto_servicio'))

@app.route('/agregar-producto')
def agregar_producto():
    return render_template('agregar_producto.html')

@app.route('/guardar-producto', methods=['POST'])
def guardar_producto():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        stock = request.form['stock']

        cursor = mysql.connection.cursor()
        query = "INSERT INTO Producto (nombre, precio, descripcion, stock) VALUES (%s, %s, %s, %s)"
        values = (name, price, description, stock)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        flash('Producto agregado correctamente')

    return redirect(url_for('producto_servicio'))

@app.route('/carrito')
def carrito():
    # Aquí debes agregar la lógica para obtener los datos del carrito y calcular el total
    carrito = [
        {
            'producto_id': 1,
            'nombre': 'Producto 1',
            'precio': 10.00,
            'cantidad': 2,
            'total': 20.00
        },
        {
            'producto_id': 2,
            'nombre': 'Producto 2',
            'precio': 15.00,
            'cantidad': 1,
            'total': 15.00
        },
        {
            'producto_id': 3,
            'nombre': 'Producto 3',
            'precio': 5.00,
            'cantidad': 4,
            'total': 20.00
        }
    ]
    total_carrito = 55.00

    return render_template('carrito.html', carrito=carrito, total_carrito=total_carrito)

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')  # Interfaz de "inicio"

if __name__ == '__main__':
    app.run(port=5000, debug=True)