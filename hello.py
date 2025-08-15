from flask import Flask

app = Flask(__name__)

Bienvenida = "¡Hello, "

texto = "Whelcome to my first page with python."


@app.route("/English/")
@app.route("/English/<nombre>") #Ruta 1
def saludo(nombre = "Brayan"):
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

@app.route("/Español/")
@app.route("/Español/<nombre>") #Ruta 2
def saludo2(nombre = "Brayan"):
    Bienvenida = "¡Hola, "
    texto = "Bienvenido a mi página web con Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

@app.route("/France/")    
@app.route("/France/<nombre>") #Ruta 3
def saludo3(nombre = "Brayan"):
    Bienvenida = "Bonjour, "
    texto = "Bienvenue sur mon site Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """
    
@app.route("/Aleman/")
@app.route("/Aleman/<nombre>")  # Ruta 4
def saludo4(nombre = "Brayan"):
    Bienvenida = "Hallo, "
    texto = "Willkommen auf meiner Python-Website."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

@app.route("/Portugues/")
@app.route("/Portugues/<nombre>")  # Ruta 5
def saludo5(nombre = "Brayan"):
    Bienvenida = "Olá, "
    texto = "Bem-vindo ao meu site Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=80)