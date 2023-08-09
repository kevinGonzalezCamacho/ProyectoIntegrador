# app.py
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

@app.route('/inicio')
def Inicio():
    return render_template('inicio.html')

@app.route('/menu', methods=['GET', 'POST'])
def menu():
    if request.method == 'POST':
        matricula = request.form['matricula']
        correo = request.form['correo']
        contrasena = request.form['contrasena']

        cursor = mysql.connection.cursor()

        # Verificar si la matrícula está en la base de datos
        query = "SELECT * FROM registro WHERE matricula = %s"
        values = (matricula,)
        cursor.execute(query, values)
        user = cursor.fetchone()

        if user:
            # Verificar si el correo coincide con la matrícula ingresada
            if user[1] == correo:
                stored_password = user[6]  # Accedemos al valor de la columna 'contrasena' por su índice (6)
                if contrasena == stored_password:
                    return redirect(url_for('Inicio'))
                else:
                    flash('Contraseña incorrecta')
            else:
                flash('Correo incorrecto para la matrícula ingresada')
        else:
            flash('Matrícula no encontrada en la base de datos')

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
        apellido_materno = request.form['apellido-materno']  # Nuevo campo para el apellido materno
        contrasena = request.form['contrasena']

        cursor = mysql.connection.cursor()
        query = "INSERT INTO registro (matricula, correo, grupo, nombre, apellido_paterno, apellido_materno, contrasena) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (matricula, correo, grupo, nombre, apellido_paterno, apellido_materno, contrasena)  # Ajustamos los valores a insertar
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
    query = "SELECT * FROM producto"
    cursor.execute(query)
    producto = cursor.fetchall()

    print(producto)
    # Cierra la conexión a la base de datos
    cursor.close()

    return render_template('misPublicaciones.html', publicaciones=producto)


@app.route('/productos')
def productos():
    cursor = mysql.connection.cursor()
    query_productos = "SELECT * FROM Producto"
    cursor.execute(query_productos)
    productos = cursor.fetchall()

    cursor.close()

    return render_template('productos.html', productos=productos)

@app.route('/agregar-producto')
def agregar_producto():
    return render_template('agregar_producto.html')

@app.route('/guardar-producto', methods=['POST'])
def guardar_producto():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        brand = request.form['brand']
        contact = request.form['contact']

        # Manejo de la imagen
        image = request.files['image']
        if image.filename != '':
            image.save("static/uploads/" + image.filename)

        cursor = mysql.connection.cursor()
        query = "INSERT INTO producto (nombre, precio, descripcion, marca, contacto, imagen) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (name, price, description, brand, contact, image.filename if image.filename != '' else None)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        flash('Producto agregado correctamente')

    return redirect(url_for('mostrar_publicaciones'))

@app.route('/buscar-producto', methods=['GET'])
def buscar_producto():
    if request.method == 'GET':
        product_name = request.args.get('product_name')

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM Producto WHERE nombre LIKE %s"
        values = ('%' + product_name + '%',)
        cursor.execute(query, values)
        productos = cursor.fetchall()
        cursor.close()

        return render_template('productos.html', productos=productos)
    
@app.route('/editar-producto/<int:producto_id>', methods=['GET', 'POST'])
def editar_producto(producto_id):
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        description = request.form['description']
        brand = request.form['brand']
        contact = request.form['contact']
        image = request.form['image']

      # ... Obtener valores del formulario y validar el precio ...

        cursor = mysql.connection.cursor()
        query = "UPDATE producto SET nombre=%s, precio=%s, descripcion=%s, marca=%s, contacto=%s, imagen=%s WHERE id_producto=%s"
        values = (name, price, description, brand, contact, image.filename if image.filename != '' else None, producto_id)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()

        flash('Producto editado correctamente')
        return redirect(url_for('mostrar_publicaciones'))  # Redirige a misPublicaciones

    cursor = mysql.connection.cursor()
    query = "SELECT * FROM producto WHERE id_producto = %s"
    values = (producto_id,)
    cursor.execute(query, values)
    producto = cursor.fetchone()
    cursor.close()

    return render_template('editar_producto.html', producto=producto)

@app.route('/eliminar-producto/<int:producto_id>', methods=['DELETE'])
def eliminar_producto(producto_id):
    cursor = mysql.connection.cursor()
    query = "DELETE FROM Producto WHERE id_producto = %s"
    values = (producto_id,)
    cursor.execute(query, values)
    mysql.connection.commit()
    cursor.close()

    return '', 204

@app.route('/servicios')
def servicios():
    cursor = mysql.connection.cursor()
    query_productos = "SELECT * FROM Servicios"
    cursor.execute(query_productos)
    servicios = cursor.fetchall()

    cursor.close()

    return render_template('servicios.html', servicios=servicios)

@app.route('/buscar-servicio', methods=['GET'])
def buscar_servicio():
    if request.method == 'GET':
        service_name = request.args.get('service_name')
        if service_name is None:
            service_name = ""

        cursor = mysql.connection.cursor()
        query = "SELECT * FROM Servicios WHERE nombre LIKE %s"
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

@app.route('/inicio')
def inicio():
    return render_template('inicio.html')  # Interfaz de "inicio"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
