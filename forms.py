from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, validators

class CafeForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    map_url = StringField('Map URL', [validators.InputRequired(), validators.URL()])
    img_url = StringField('Image URL', [validators.InputRequired(), validators.URL()])
    location = StringField('Location', [validators.InputRequired()])
    has_sockets = BooleanField('Has Sockets')
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has WiFi')
    can_take_calls = BooleanField('Can Take Calls')
    seats = StringField('Seats', [validators.InputRequired()])
    coffee_price = StringField('Coffee Price', [validators.InputRequired()])
    submit = SubmitField('Add Cafe')
