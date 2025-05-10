# C:\Users\ianes\Desktop\AS Cloud\app\cars\forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class CarForm(FlaskForm):
    name         = StringField('Nome do Carro', validators=[DataRequired(), Length(max=100)])
    photo       = StringField('URL da Foto', validators=[DataRequired()])
    description = TextAreaField('Descrição / História', validators=[DataRequired()])
    start_year  = IntegerField('Ano Início Produção', validators=[DataRequired()])
    end_year    = IntegerField('Ano Fim Produção', validators=[DataRequired()])
    horsepower  = IntegerField('Potência (cv)', validators=[DataRequired()])
    torque      = IntegerField('Torque (Nm)', validators=[DataRequired()])
    top_speed   = IntegerField('Velocidade Máx. (km/h)', validators=[DataRequired()])
    drive_type  = StringField('Tipo de Tração', validators=[DataRequired()])
    transmission= StringField('Câmbio', validators=[DataRequired()])
    submit      = SubmitField('Criar Carro')
