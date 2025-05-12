# C:\Users\ianes\Desktop\AS Cloud\app\auth\forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class RegistrationForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(3, 80)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 128)])
    confirm = PasswordField('Confirme a senha',
                            validators=[DataRequired(), EqualTo('password', message='As senhas não coincidem.')])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    username = StringField('Usuário', validators=[DataRequired(), Length(3, 80)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(6, 128)])
    submit = SubmitField('Entrar')
