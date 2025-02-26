from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class PostForm(FlaskForm):
    title = StringField('Título', validators=[DataRequired(), Length(max=100)])
    content = TextAreaField('Conteúdo', validators=[DataRequired()])
    submit = SubmitField('Criar Post')