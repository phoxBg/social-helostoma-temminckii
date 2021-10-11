from flask import Flask, render_template, request, url_for, flash, redirect, Request
import yagmail
import utils
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Se crea una lista de usuarios para el tema de logica algoritmica simple.
usuarios_sistema=["Brayan","Fernando","Sergio","Giovanny","Jairo"]

#Se crea un dicicionario de publicaciones con la finalidad de validar la algoritmica simple
lista_publicaciones1={
    123:"Publicacion No 1",
    124:"Publicacion No 2",
    125:"Publicacion No 3",
    126:"Publicacion No 4",
    127:"Publicacion No 5",
    128:"Publicacion No 6",
    129:"Publicacion No 7",
    130:"Publicacion No 8",
    131:"Publicacion No 9",
}

lista_publicaciones={
    123:{'titulo':"publicaciones #1",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    124:{'titulo':"publicaciones #2",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    125:{'titulo':"publicaciones #3",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    126:{'titulo':"publicaciones #4",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    127:{'titulo':"publicaciones #5",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    128:{'titulo':"publicaciones #6",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    129:{'titulo':"publicaciones #7",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    130:{'titulo':"publicaciones #8",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
    131:{'titulo':"publicaciones #9",'cuerpo': "Publicacion Cuerpo",'imagenes':['img 1','img 2','img 3','img 4']},
}

#Se crea un dicicionario de publicaciones con la finalidad de validar la algoritmica simple
lista_mensaje1={
    223:"Mensaje No 1",
    224:"Mensaje No 2",
    225:"Mensaje No 3",
    226:"Mensaje No 4",
    227:"Mensaje No 5",
    228:"Mensaje No 6",
    229:"Mensaje No 7",
    230:"Mensaje No 8",
    231:"Mensaje No 9",
}

lista_mensaje={
    223:{'mensaje':"Mensaje #1",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    224:{'mensaje':"Mensaje #2",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    225:{'mensaje':"Mensaje #3",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    226:{'mensaje':"Mensaje #4",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    227:{'mensaje':"Mensaje #5",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    228:{'mensaje':"Mensaje #6",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    229:{'mensaje':"Mensaje #7",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    230:{'mensaje':"Mensaje #8",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
    231:{'mensaje':"Mensaje #9",'cuerpo': "Mensaje Cuerpo",'calificaciones':['img Calificacion 1','img Calificacion 2','img Calificacion 3','img Calificacion 4']},
}


# Se crea esta variable para probar el inicio de sesion.
sesion_iniciada=False

# Ruta Raiz ----------------------
@app.route("/", methods=["GET"])

# Index ----------------------
@app.route("/index", methods=["GET"])
def index():
    #Si ya inicio Sesion ->Lista de publicaciones Feed.
    #Sino -> Bienvenida
    #return render_template("register.html")
    return render_template("index.html", sesion_iniciada=sesion_iniciada)

# Ingreso ----------------------
@app.route("/ingreso",methods=["GET","POST"])
def ingreso():
    global sesion_iniciada
    if request.method=="GET":
        return render_template("login.html")
    else:
        sesion_iniciada=True
        return redirect('/index')

# Salir ----------------------
@app.route("/salir",methods=["GET","POST"])
def salir():
    global sesion_iniciada
    sesion_iniciada=False
    return redirect('/index')

# Perfil ----------------------
@app.route("/perfil",methods=["GET","POST"])
def perfil():
        return "Pagina de Perfil de usuario"  #perfil.html

# Perfil usuarios ---------------------------
@app.route("/usuario/<id_usuario>",methods=["GET"])
def usuario_informacion(id_usuario):
    #validacion simple de usuario ..............................................
    if id_usuario in usuarios_sistema:
        return f"Pagina del Perfil del usuario {id_usuario}"    #validacion simple de usuario
    else:
        return f"Error, el usuario {id_usuario} no exite en la base de datos"

# Perfil admin  ..............
@app.route("/admin/<id_admin>",methods=["GET"])
def admin_informacion(id_admin):
    if id_admin in usuarios_sistema:
        return f"Pagina del Perfil del usuario Admin {id_admin}"   #validacion simple de Perfil admin
    else:
        return f"Error, el usuario {id_admin} no exite en la base de datos"

# Perfil superadmin ............
@app.route("/superadmin/<id_superadmin>",methods=["GET"])
def superadmin_informacion(id_superadmin):
    if id_superadmin in usuarios_sistema:
        return f"Pagina del Perfil del usuario Superadmin {id_superadmin}"  #validacion simple de Perfil superadmin
    else:
        return f"Error, el usuario {id_superadmin} no exite en la base de datos"

# Publicaciones --------------
@app.route("/publicaciones",methods=["GET"])
def publicacion():
    global sesion_iniciada
    #return "Pagina de todas las publicaciones"  #publicaciones.html .....................
    return render_template("publicaciones.html", sesion_iniciada=sesion_iniciada,lista_publicaciones=lista_publicaciones)

# Detalle de las publicaciones -----------
@app.route("/detalle_pub/<id_publicacion>",methods=["GET","POST"])
def detalle_pub(id_publicacion):
    try:
        id_publicacion=int(id_publicacion)
    except Exception as e:
        id_publicacion=0

    if id_publicacion in lista_publicaciones:
        return lista_publicaciones[id_publicacion]
    else:
        return f"Error, la publicacion {id_publicacion} no exite en la base de datos"
        #return f"Pagina detalle de la publicacion {id_publicacion}"  #detalla_pub.html

# Busqueda de usuario ---------------------------
@app.route("/busqueda/<id_usuario>",methods=["GET","POST"])
def busqueda_usuario(id_usuario):
    if id_usuario in usuarios_sistema:
        return f"El usuario que buscas Existe: {id_usuario}, en la Base de Datos."
    else:
        return f"El usuario que buscas no existe: {id_usuario}"

# Mensajes ---------------------
@app.route("/msg",methods=["GET"])
def msg():
    global sesion_iniciada
    #return f"Pagina de Mensajes"  #msg.html
    return render_template("mensajes.html", sesion_iniciada=sesion_iniciada,lista_mensaje=lista_mensaje)

# Mensajes privados --------------
@app.route("/msg_privado/<id_msg>",methods=["GET","POST"])
def msg_privado(id_msg):
    try:
        id_msg=int(id_msg)
    except Exception as e:
        id_publicacion=0

    if id_msg in lista_mensaje:
        return lista_mensaje[id_msg]
    else:
        return f"Error, el mensaje {id_msg} no exite en la base de datos"
    #return f"Pagina - Mensaje privado : {id_msg}"  #msg_privado.html

# Registrar ---------------------------
@app.route("/register" , methods=["GET","POST"])
def register():
    global sesion_iniciada
    try:
        if request.method=="POST":
            user1=request.form["username"]
            pass1=request.form["password"]
            c_pass1=request.form["c_password"]
            email=request.form["correo"]
            error = None

            if not utils.isUsernameValid(user1):
                error ="El usuario no es correcto"
                flash(error)
                return render_template("register.html")

            if not utils.isPasswordValid(pass1):
                error="Password invalido"
                flash(error)
                return render_template("register.html")

            if not utils.isPasswordValid(c_pass1):
                error="Password invalido"
                flash(error)
                return render_template("register.html")

            if (c_pass1 !=pass1):
                error="Password no coincide"
                flash(error)
                return render_template("register.html")

            if not utils.isEmailValid(email):
                error="Correo invalido"
                flash(error)
                return render_template("register.html")

            yag=yagmail.SMTP("pruebamintic2022","Jmd12345678")
            print("Paso por yag.")
            yag.send(to=email, subject="Activa tu cuenta", contents="Bienvenido, usa este link para activar tu cuenta")
            flash("Revisa tu correo para activar tu cuenta")
            return render_template("login.html")

        return render_template("register.html")
    except:
        return render_template("register.html")

if __name__=='__main__':
    app.run(debug=True, port=8080)
