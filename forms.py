from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField

class PetForm(FlaskForm):
    """ Form for adding new pet """
    name = StringField("Pet name")
    species = StringField("Pet species")
    photo_url = StringField("Photo URL")
    age = IntegerField("Pet age")
    notes = StringField("Additional Notes")