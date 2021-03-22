from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField, validators, IntegerField, FloatField, SubmitField, 
from wtforms.validators import DataRequired, Email, InputRequired


# options for the property type 

property_types = ['House', 'Apartment']

# WTForm for a new property view/page

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    num_bedrooms = StringField('Number Of Bedrooms', validators=[DataRequired()])
    num_bathrooms = StringField('Number of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    types = SelectField('Type', choices=property_types)
    description = TextAreaField('Description', widget=TextArea(row=10, cols=15))
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    submit = SubmitField('Submit')

