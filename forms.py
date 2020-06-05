from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import InputRequired, Optional, URL

class AddPetForm(FlaskForm):

    name = StringField("Pet Name", validators=[InputRequired(), validate_name])
    species = StringField("Species", validators=[InputRequired()])
    photo_url = StringField("Pet Name", validators=[Optional(), URL()])
    age = StringField("Pet Name", validators=[InputRequired(), validate_age])
    notes = StringField("Pet Name", validators=[Optional()])
    available = BooleanField("Pet Name", validators=[InputRequired()])

    def validate_name(form, field):
        if field.data not in ['cat', 'dog', 'porcupine']:
            raise ValidationError('Your pet is not a cat, dog, or porcupine!')

    def validate_age(form, field):
        if field.data not in ['baby', 'young', 'adult', 'senior']:
            raise ValidationError('Your pet\'s age is wrong! Valid ages are: baby, young, adult, senior.')
