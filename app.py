from flask import Flask, render_template, redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

connect_db(app)
db.create_all()

toolbar = DebugToolbarExtension(app)

@app.route('/')
def show_list_pets():
    pets = Pet.query.all()
    return render_template('pets-list.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        flash(f"New pet added!")
        return redirect('/add')
    
    else:
        return render_template('add-form.html', form=form)