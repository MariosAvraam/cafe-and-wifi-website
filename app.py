from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import CafeForm
from flask_bootstrap import Bootstrap5
from os import getenv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
Bootstrap5(app)

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
    search_query = request.args.get('search', '')
    page = request.args.get('page', 1, type=int)
    per_page = 10
    cafes_query = Cafe.query.filter(Cafe.name.like(f'%{search_query}%'))
    cafes = cafes_query.paginate(page=page, per_page=per_page, error_out=False)
    return render_template('index.html', cafes=cafes.items, pagination=cafes)


@app.route('/add_cafe', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
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
            coffee_price='£' + request.form['coffee_price'],
        )

        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_cafe.html', form=form)

@app.route('/delete_cafe/<int:cafe_id>')
def delete_cafe(cafe_id):
    cafe_to_delete = db.get_or_404(Cafe, cafe_id)
    if cafe_to_delete:
        db.session.delete(cafe_to_delete)
        db.session.commit()
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
