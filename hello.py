from flask import Flask

app = Flask(__name__)

Bienvenida = "¡Hello, "

texto = "Whelcome to my first page with python."

nombres = []

#Comentario
@app.get("/English/")
#@app.route("/English/<nombre>") #Ruta 1
def saludo(nombre = "Brayan"):
    return nombres

@app.post("/Español/")
@app.post("/Español/<nombre>")
#@app.route("/Español/<nombre>") #Ruta 2
def saludo2(nombre = "Brayan"):
    nombres.append(nombre)
    Bienvenida = "¡Hola, "
    texto = "Bienvenido a mi página web con Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

@app.put("/France/")
@app.put("/France/<nombre>")
#@app.route("/France/<nombre>") #Ruta 3
def saludo3(nombre = "Brayan"):
    nombres[0] = nombre
    Bienvenida = "Bonjour, "
    texto = "Bienvenue sur mon site Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """
    
@app.delete("/Aleman/")
#@app.route("/Aleman/<nombre>")  # Ruta 4
def saludo4(nombre = "Brayan"):
    nombres.remove(nombre)
    Bienvenida = "Hallo, "
    texto = "Willkommen auf meiner Python-Website."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

@app.route("/Portugues/")
#@app.route("/Portugues/<nombre>")  # Ruta 5
def saludo5(nombre = "Brayan"):
    Bienvenida = "Olá, "
    texto = "Bem-vindo ao meu site Python."
    return f"""
        <h1>{Bienvenida + nombre}</h1>
        <p>{texto}</p>
    """

if __name__ == "__main__":
    app.run(debug = True)

#app.run(debug = True, host='0.0.0.0', port=80)