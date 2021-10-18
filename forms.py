from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
from wtforms.validators import Length, Email





'''class formEstudiante(FlaskForm):
    documento=StringField('Documento', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'Identificación', 'class':'form_control'})
    nombre=StringField('Nombre', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'Nombre', 'class':'form_control'})
    ciclo=SelectField('Ciclo', choices=[('Python'), ('Java'),('Web')])
    sexo=StringField('Sexo', validators=[DataRequired(message="no dejar Vacio")], render_kw={'placeholder':'M/F', 'class':'form_control'})
    estado=BooleanField('Estado')

    # botones
    enviar=SubmitField('Enviar', render_kw={'onmouseover':'guardarEst()', 'class':'form_boton'})
    consultar=SubmitField('Consultar', render_kw={'onmouseover':'consultarEst()', 'class':'form_boton'})
    listar=SubmitField('Listar', render_kw={'onmouseover':'listarEst()', 'class':'form_boton'})
    actualizar=SubmitField('Actualizar', render_kw={'onmouseover':'actualizarEst()', 'class':'form_boton'})
    eliminar=SubmitField('eliminar', render_kw={'onmouseover':'eliminarEst()', 'class':'form_boton'})

    # Eventos

class  formLogin(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario'} )
    clave = PasswordField('Clave', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Contraseña', 'id':'password'} )
    enviar = SubmitField('Enviar', render_kw={'class':'form_boton', 'onmouseover':'consultar_login()', 'class':'form_boton' })
    guardar = SubmitField('Guardar', render_kw={'class':'form_boton','onmouseover':'crear_login()', 'class':'form_boton'} )
'''

class  formRegister(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired(message='No dejar vacio')], render_kw={'placeholder':'Usuario', 'class':'input','type':'text', 'id':'username', 'autocomplete':'username', 'required':'true', 'placeholder':'pepitoperez'} )
    correo = EmailField('correo', validators=[DataRequired(message='No dejar vacio')],render_kw={'class':'input', 
	'type':'text',
	'id':'email',
        'maxlength':'100',
        'placeholder':'e.g. alex@example.com',
        'autocomplete':'email',
        'required':'true',
        'pattern': '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$',
        'style':'text-transform: lowercase',
        'onkeyup':'javascript:this.value:this.value.toLowerCase();'})
    clave = PasswordField('Contraseña', validators=[DataRequired(message='No dejar vacio')], render_kw={'class':'input',
        'type':'password',
        'id':'password',
        'placeholder':'Contraseña',
        'required':'true',
        'minlength':'6'} )
    clave1 = PasswordField('Confirmar contraseña', validators=[DataRequired(message='No dejar vacio')], render_kw={'class':'input',
        'type':'password',
        'id':'password1',
        'placeholder':'Confirmar contraseña',
        'required':'true',
        'minlength':'6'} )
    estado=BooleanField('Estado',render_kw={'type':'checkbox', 'required':'true'})    
    guardar = SubmitField('Registrate!', render_kw={'onmouseover':'crear_register()',  'class':'button is-link is-fullwidth', 'type':'submit', 'value':'Registrate!'} )    

  