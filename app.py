from flask import Flask, escape, request,render_template, url_for     #Importar la libreria

app = Flask(__name__) #Inicializamos la app con el nombre.

@app.route ("/")

def hola(): # Definimos que en la ruta de inicio sera aplicada la funcion hola
    return "Hi Penguins!" #Returna Hi Penguins


@app.route ("/coach")
def hola_coaches():
    nombre = "Enzo"
    devolver = request.args.get ("nombre", nombre)

    return f'Hola, {escape(devolver)} '

@app.route ("/inicio") #Creamos la ruta de inicio 
def inicio ():
    return render_template("inicio.html")
@app.route ('/contacto')
def contacto ():
     return render_template('contacto.html')

app.run(debug=True) # Para ejecutar
