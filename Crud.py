from flask import Flask

app = Flask(__name__)

personas = [
    ["Brayan", "123456789"],
    ["Camila", "987654321"],
    ["Juan", "555555555"]
]

#Comentario
@app.get("/English/")
#@app.route("/English/<nombre>") #Ruta 1
def saludo(nombre = "Brayan"):
    return nombres

@app.post("/Espanol/")
@app.post("/Espanol/<nombre>")
#@app.route("/Español/<nombre>") #Ruta 2
def saludo2(nombre = "Brayan"):
    nombres.append(nombre)


@app.put("/France/")
@app.put("/France/<nombre>")
#@app.route("/France/<nombre>") #Ruta 3
def saludo3(nombre = "Brayan"):
    nombres[0] = nombre

    
@app.delete("/Aleman/")
#@app.route("/Aleman/<nombre>")  # Ruta 4
def saludo4(nombre = "Brayan"):
    nombres.remove(nombre)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
#app.run(debug = True)

#app.run(debug = True, host='0.0.0.0', port=80)