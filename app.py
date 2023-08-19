from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    map_url = db.Column(db.String(500))
    img_url = db.Column(db.String(500))
    location = db.Column(db.String(150))
    has_sockets = db.Column(db.Boolean, default=False)
    has_toilet = db.Column(db.Boolean, default=False)
    has_wifi = db.Column(db.Boolean, default=False)
    can_take_calls = db.Column(db.Boolean, default=False)
    seats = db.Column(db.String(50))
    coffee_price = db.Column(db.String(50))


@app.route('/')
def index():
    result = db.session.execute(db.select(Cafe))
    cafes = result.scalars()
    return render_template('index.html', cafes=cafes)

@app.route('/add_cafe', methods=['GET', 'POST'])
def add_cafe():
    if request.method == "POST":
        new_cafe = Cafe(
            name=request.form['name'],
            map_url=request.form['map_url'],
            img_url=request.form['img_url'],
            location=request.form['location'],
            has_sockets=bool(request.form.get('has_sockets')),
            has_toilet=bool(request.form.get('has_toilet')),
            has_wifi=bool(request.form.get('has_wifi')),
            can_take_calls=bool(request.form.get('can_take_calls')),
            seats=request.form['seats'],
            coffee_price=request.form['coffee_price']
        )

        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_cafe.html')

@app.route('/delete_cafe/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
