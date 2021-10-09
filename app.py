from flask import Flask, render_template, request, url_for, flash, redirect, Request
import yagmail
import utils
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

#Se crea una lista de usuarios para el tema de logica algoritmica simple.
usuarios_sistema=["Braya","Fernando","Sergio","Giovanny","Jairo"]

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


if __name__=='__main__':
    app.run(debug=True, port=8080)  
