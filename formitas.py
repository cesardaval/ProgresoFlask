from wtforms import Form
from wtforms import TextField,StringField
from wtforms.fields.html5 import EmailField
from wtforms import validators
class CommentForm(Form):
    username = StringField('username',[ validators.Required(message="el usuario es requerido"),
        validators.Length(min=4, max=25,message="ingrese un usuario valido")
        
        ])
    email = EmailField('email',[validators.Required(message=()
    )])
    comment = TextField('comentario')
    
    honeypot = TextField('')




