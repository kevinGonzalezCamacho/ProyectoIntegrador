from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('menu.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Aquí puedes agregar el código para procesar el formulario de registro
        # y guardar los datos en una base de datos, si es necesario.
        
        # Después de procesar el formulario, redirige al usuario a la página de menú
        return redirect(url_for('index'))
    else:
        return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
