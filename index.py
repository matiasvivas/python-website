from flask import Flask, render_template

app = Flask(__name__)

# Creando las rutas de menu de la aplicaicon
@app.route('/test')
def test():
    return "Principal"

@app.route('/test/informacion/')
def informacion_test():
    return "Informacion"

# Funciones para renderizar la pagina (investigar como embeber html)
@app.route('/')
def principal():
    return render_template("principal.html")

@app.route('/informacion', strict_slashes=False)
def informacion():
    return render_template("informacion.html")

# Verificar si estamos en el archivo principal
#Ejecutar run desde app para permanecer el estado activo de la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
