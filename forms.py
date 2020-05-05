from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField
from wtforms.validators import InputRequired, Optional, URL,  NumberRange

class AddPetForm(FlaskForm):
    """ Form for adding new pet """
    name = StringField("Pet name", validators=[InputRequired(message='Pet name is required!')])
    species = SelectField('Pet species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Pet age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Available?", default=True)

class EditPetForm(FlaskForm):
    """ Form for editing pets """
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = StringField("Additional Notes", validators=[Optional()])
    available = BooleanField("Available?", default=True)