from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, DecimalField, IntegerField, validators
from wtforms.widgets import TextInput

class PoundTextInput(TextInput):
    """Custom TextInput widget that adds a £ symbol as placeholder."""
    def __call__(self, field, **kwargs):
        kwargs.setdefault('placeholder', '£0.00')
        return super(PoundTextInput, self).__call__(field, **kwargs)

class CafeForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    map_url = StringField('Map URL', [validators.InputRequired(), validators.URL()])
    img_url = StringField('Image URL', [validators.InputRequired(), validators.URL()])
    location = StringField('Location', [validators.InputRequired()])
    has_sockets = BooleanField('Has Sockets')
    has_toilet = BooleanField('Has Toilet')
    has_wifi = BooleanField('Has WiFi')
    can_take_calls = BooleanField('Can Take Calls')
    seats = StringField('Seats', [validators.DataRequired()])
    coffee_price = StringField('Coffee Price', [validators.Regexp(r'^\d+(\.\d{1,2})?$', message="Enter a valid price")])
    submit = SubmitField('Add Cafe')
