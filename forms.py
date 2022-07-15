from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired

#class Namn(FlaskForm):
#    namn = StringField('1. Namnge ert hackaton.', validators= [DataRequired()])

class Tema(FlaskForm):
    tema = StringField('Börja med att välja en utmaning för ert hackaton.', validators= [DataRequired()])
    submit = SubmitField('+')

class Deltagare(FlaskForm):
    deltagare = IntegerField('Hur många kommer att delta?', validators=[DataRequired()])
    submit = SubmitField('+')

class Längd(FlaskForm):
    längd = IntegerField('Hur många timmar finns till förfogande? Ange tiden i hela timmar.', validators=[DataRequired()])
    submit = SubmitField('+')

class Budget(FlaskForm):
    budget = IntegerField('Vad är er budget?', validators=[DataRequired()])
    submit = SubmitField('+')

class Plats(FlaskForm):
    plats = StringField('Var tänker ni ordna ert hackaton?', validators=[DataRequired()])
    submit = SubmitField('+')

class Jury(FlaskForm):
    jury = IntegerField('Hur många jurymedlemmar ska ni ha?', validators=[DataRequired()])
    #jury =  RadioField('6. Ska ni ha en jury?', choices=['Ja', 'Nej'], validators=[InputRequired()])
    submit = SubmitField('+')

class JuryNamn(FlaskForm):
    juryNamn = StringField('Vilka är era jurymedlemmar?', validators=[DataRequired()])
    submit = SubmitField('+')

class Språk(FlaskForm):
    språk = IntegerField('Hur många språk ingår i ert hackaton?', validators=[DataRequired()])
    submit = SubmitField('+')
