from flask import Flask

app = Flask(__name__)

DataBase = [
    ["Brayan", 123, "brayan@gmail.com" ],
]

@app.get("/Read/")
@app.get("/Read/<id>")
def leer(id = 0):
    if(id == 0):
        resultado = "Usuarios Registrados:\n"
        for usuario in DataBase:
            resultado += f"{usuario}\n"
        return resultado
    else:
        for usuario in DataBase:
            if usuario[1] == int(id):   # columna 1 = id
                return f"Nombre: {usuario[0]} \nID: {usuario[1]} \nEmail: {usuario[2]}"
        return "Id de usuario no encontrado, por favor verifiquelo e intentelo nuevamnete"

@app.post("/Create/")
@app.post("/Create/<nombre>")
@app.post("/Create/<nombre>/<id>")
@app.post("/Create/<nombre>/<id>/<email>")
def crear(nombre = "", id = "", email = ""):
    if(nombre != "" and id != "" and email != ""):
        DataBase.append([nombre, int(id), email])
        return "Usuario: " + nombre + " Registrado con exito"
    else: 
        return f''' Recuerde que debe ingresar los datos completos
            \n luego de la url debe poner /su nombre/su id/su email
            \n por favor intentelo nuevamente
        '''


@app.put("/Update/")
@app.put("/Update/<nombre>")
@app.put("/Update/<nombre>/<id>")
@app.put("/Update/<nombre>/<id>/<email>")
def actualizar(nombre = "", id = "", email = ""):
    if(nombre != "" and id != "" and email != ""):
        for i, usuario in enumerate(DataBase):
            if usuario[1] == int(id):  
                DataBase[i] = [nombre, int(id), email] 
                return f"Usuario: {nombre} \nActualizado Correctamnete"
        return "Id de usuario no encontrado en la base de datos, para actulizar por favor verifiquelo e intentelo nuevamnete"
    else: 
        return f''' Recuerde que debe ingresar los datos completos para poder actulizar la informacion de un usuario
            \n luego de la url debe poner /su nombre/su id/su email
            \n por favor intentelo nuevamente
        '''

    
@app.delete("/Delete/")
@app.delete("/Delete/<id>")
def eliminar(id = ""):
    if(id != ""):
        for usuario in DataBase:
                if usuario[1] == int(id):   # columna 1 = id
                    DataBase.remove(usuario)
                    return f"Usuario: {usuario[0]} \nEliminado Correctamnete"
        return "Id de usuario no encontrado, para eliminar por favor verifiquelo e intentelo nuevamnete"
    else:
        return f''' Para eliminar un usuario debe ingresar el id
            \n luego de la url debe poner /id
            \n por favor intentelo nuevamente
        '''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
    
#app.run(debug = True)

#app.run(debug = True, host='0.0.0.0', port=80)