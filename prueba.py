from flask import Flask, request

app = Flask(__name__)

usuarios = []  # Lista para guardar los nombres

@app.get("/")
def inicio():
    return "Bienvenido!"

# READ (mostrar usuarios)
@app.get("/usuarios")
def listar():
    return f"Usuarios: {usuarios}"

# CREATE (crear usuario)
@app.post("/crear")
def crear():
    nombre = request.form.get("nombre", "anónimo")
    usuarios.append(nombre)
    return f"Usuario {nombre} agregado"

# UPDATE (actualizar usuario)
@app.put("/actualizar")
def actualizar():
    viejo = request.form.get("viejo")
    nuevo = request.form.get("nuevo")
    if viejo in usuarios:
        usuarios.remove(viejo)   # quitamos el viejo
        usuarios.append(nuevo)   # ponemos el nuevo
        return f"Usuario {viejo} ahora es {nuevo}"
    return f"{viejo} no existe"

# DELETE (borrar usuario)
@app.delete("/borrar")
def borrar():
    nombre = request.form.get("nombre")
    if nombre in usuarios:
        usuarios.remove(nombre)
        return f"Usuario {nombre} eliminado"
    return f"{nombre} no existe 25"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    
#app.run(debug=True, host="0.0.0.0")