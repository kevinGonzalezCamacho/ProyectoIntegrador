from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "systemshop"  

app.secret_key='mysecretkey'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario-registro', methods=['POST'])
def guardar():
    if request.method == 'POST':
        VDescripcion = request.form['txtDescripcion']
        VFecha_inicio = request.form['txtFecha_inicio']
        VFecha_final = request.form['txtFecha_final']
        
        cs = mysql.connection.cursor()
        cs.execute('INSERT INTO systemshop (Descripcion, Fecha_inicio, Fecha_final) VALUES (%s, %s, %s)', (VDescripcion, VFecha_inicio, VFecha_final))
        mysql.connection.commit()
        cs.close()
        
        flash('Album Agregado Correctamente')
    return redirect(url_for('index'))

@app.route('/eliminar')
def eliminar():
    return "Se eliminó el álbum de la base de datos."


if __name__ == '__main__':
    app.run(port=5000, debug=True)